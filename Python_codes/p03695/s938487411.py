N = int(input())
A = sorted(map(int, input().split()))

colors = [0] * 9
for a in A:
    idx = a // 400
    if idx >= 8:
        idx = 8
    colors[idx] += 1
ans = 0
for i in range(8):
    if colors[i] > 0:
        ans += 1
max_ans = ans
if colors[8] > 0:
    max_ans += colors[8]

if ans == 0 and max_ans > 0:
    ans += 1
print(ans, max_ans)