def factorial(x, mod=10**9+7):
    # x!
    # 階乗
    # ex) factorial(5) = 120
    tmp = 1
    for i in range(1, x+1):
        tmp = (tmp * i) % mod
    return tmp


N ,M = map(int, input().split())
mod = 1000000007

if N==M:
    print((2*factorial(N)**2) % mod )
elif abs(N-M)==1:
    print((factorial(N)*factorial(M))%mod)
else:
    print(0)

