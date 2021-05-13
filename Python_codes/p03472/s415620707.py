N, H = map(int, input().split())

Bs = []
max_swing_i = 0
max_swing = 0
throw_when_max_swing = 0
for i in range(N):
    a, b = map(int, input().split())
    if a > max_swing:
        max_swing = a
        throw_when_max_swing = b
        max_swing_i = i

    Bs.append(b)

# 取りのぞいて並び替える
#Bs = Bs.pop(max_swing_i)
Bs.sort(reverse=True)

ans = 0
for i in range(len(Bs)):
    if H <= 0 or Bs[i] < max_swing:
        break

    H -= Bs[i]
    ans += 1

if H > 0:
    if H % max_swing == 0:
        ans += H // max_swing
    else:
        ans += H // max_swing + 1

print(ans)
