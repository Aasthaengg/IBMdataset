import sys
input = sys.stdin.readline


n, c = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(n)]
half = c//2

DP_left = {}
DP_right = {}
ans = []
# 時計まわりでスタート地点からposまでの最高値
energy = 0
maxim = 0
prev = 0
for pos, cal in sushi:
    lost = pos - prev
    energy += cal - lost
    maxim = max(maxim, energy)
    DP_left[pos] = maxim
    prev = pos
ans.append(maxim)

# 反時計回り
energy = 0
maxim = 0
prev = c
for pos, cal in sushi[::-1]:
    lost = prev - pos
    energy += cal - lost
    maxim = max(maxim, energy)
    DP_right[pos] = maxim
    prev = pos
ans.append(maxim)

# 時計まわりで途中でターン
energy = 0
maxim = 0
prev = 0
for idx, (pos, cal) in enumerate(sushi):
    if idx == n-1:
        break
    if pos > half:
        break
    lost = pos - prev
    energy += cal - lost
    next_pos, _ = sushi[idx+1]
    back_cost = pos
    result = energy - back_cost + DP_right[next_pos]
    maxim = max(maxim, result)
    prev = pos
ans.append(maxim)

# 反時計まわりで途中でターン
energy = 0
maxim = 0
prev = c
for idx, (pos, cal) in enumerate(sushi[::-1], 1):
    if idx == n:
        break
    if pos < half:
        break
    lost = prev - pos
    energy += cal - lost
    back_cost = c - pos
    next_pos, _ = sushi[-idx-1]
    result = energy - back_cost + DP_left[next_pos]
    maxim = max(maxim, result)
    prev = pos
ans.append(maxim)

print(max(ans))