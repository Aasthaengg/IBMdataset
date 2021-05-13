d = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

inf = 10**9
dp = [-inf]*(N+1)
dp[0] = 0


for a in A:
    for j in range(d[a], N + 1):
        dp[j] = max(dp[j], dp[j - d[a]] + 1)

ans = ""
remain = dp[N]
match = N
while match > 0:
    for a in A:
        if match - d[a] < 0:
            continue
        if dp[match - d[a]] == remain - 1:
            ans += str(a)
            match -= d[a]
            remain -= 1
            break

print(ans)
