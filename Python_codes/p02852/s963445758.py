N, M = map(int, input().split())
S = input()

dp = [-1] * (N + M + 1)
dp[N] = 0
pos = N

while pos > 0:
    dist = dp[pos]
    tmp = pos

    for i in range(1, M + 1):
        if pos - i < 0:
            break
        if S[pos - i] == "0":
            dp[pos - i] = dist + 1
            tmp = pos - i
    if pos == tmp:
        break
    pos = tmp

if dp[0] == -1:
    print(-1)
    exit()

ans = []
cnt = dp[0]
pos = 0
while cnt > 0:
    for i in range(1, M + 1):
        if dp[pos + i] + 1 == cnt:
            ans.append(i)
            pos += i
            cnt -= 1
            break

print(*ans, sep=" ")
