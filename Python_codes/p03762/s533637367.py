
N,M = map(int, input().split())

X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 10**9+7


sum_x = 0
sum_y = 0
for i in range(N):
    sum_x += (i - (N - i - 1))*X[i] % MOD

for j in range(M):
    sum_y += (j - (M - j - 1))*Y[j] % MOD


print(sum_x*sum_y%MOD)
