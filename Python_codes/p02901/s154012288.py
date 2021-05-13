n, m = map(int, input().split())
a = []
b = []
c = []
checker = [0]*n
for _ in range(m):
    ai, bi = map(int, input().split())
    ci = list(map(int, input().split()))
    ci_int = 0
    for hako in ci:
        hako -= 1
        ci_int += 2**hako
        if checker[hako] == 0:
            checker[hako] = 1
    a.append(ai)
    b.append(bi)
    c.append(ci_int)
#print(a)
#print(b)
#print(c)
if sum(checker) != n:
    print(-1)
    exit()

dp = [[float("inf")]*(2**n) for _ in range(m+1)]
#dp[i][S]はi番目までのカギをいくつか使ってSになるようなコストの最小値
#Sは2進数で表現できる。例）１と３の箱が開けられる状態->0b101
dp[0][0] = 0
for i in range(m):
    for s in range(2**n):
        # i番目のカギを使用しない場合
        dp[i+1][s] = min(dp[i+1][s], dp[i][s])
        # 使用する場合
        dp[i+1][s | c[i]] = min(dp[i+1][s|c[i]], dp[i][s] + a[i])
print(dp[m][2**n-1])