import sys
input = sys.stdin.readline

N = int(input())
C = [int(input()) for _ in range(N)]
mod = 10 ** 9 + 7

newC = []
while C:
    c = C.pop()
    if not newC or newC[-1] != c:
        newC.append(c)
N = len(newC)

seen = [0] * (2*10 ** 5 + 10)
dp = [0] * (N + 1)
dp[0] = 1
seen[newC[0]] = 1

for i, c in enumerate(newC[1:], start=1):
    cnt = seen[c]
    seen[c] = (seen[c] + dp[i - 1]) % mod
    dp[i] = (dp[i - 1] + cnt) % mod

ans = dp[N - 1]
print(ans)
