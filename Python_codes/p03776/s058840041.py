#組み合わせ
def comb(a, b):
    if b > a - b:
        return comb(a, a-b)
    ansMul = 1
    ansDiv = 1
    for i in range(b):
        ansMul *= a - i
        ansDiv *= i + 1

    ans = ansMul // ansDiv
    return ans

N, A, B = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if j > i:
            continue
        dp[i+1][j+1] = max(dp[i+1][j+1], (dp[i][j] * j + v[i]) / (j + 1))
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

ans = 0
for i in range(A, B+1):
    ans = max(ans, dp[N][i])

v.sort()
v.reverse()

c = v.count(v[0])
cnt = 0
if v[0] == v[A-1]:
    for i in range(A, B+1):
        if c < i:
            break
        cnt += comb(c, i)
else:
    a = v[:A].count(v[A-1])
    all_a = v.count(v[A-1])
    cnt = comb(all_a, a)

print(ans)
print(cnt)
