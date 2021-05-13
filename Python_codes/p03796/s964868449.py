MOD = 1000000007
N = int(input())
res = 1
for i in range(N):
    res *= i + 1
    res %= MOD
print(res)