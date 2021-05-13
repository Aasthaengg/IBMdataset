N = int(input())
n = 0
a = n ** 2 + n - 2 * N
# 上から抑える
while a < 0:
    n += 1
    a = n ** 2 + n - 2 * N

score = 0
ans = []
for i in reversed(range(1, n + 1)):
    if score + i <= N:
        score += i
        ans.append(i)
    if score == N:
        break

for i in ans:
    print(i)