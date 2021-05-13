def memfact(a,m):
    temp = 1
    yield temp
    for i in range(1,a+1):
        temp = temp * i % m
        yield temp
def comb(n,r,m):
    if r == 0: return 1
    return memf[n]*pow(memf[r],m-2,m)*pow(memf[n-r],m-2,m)

n,k = map(int, open(0).read().split())
dp = [0] * n
dp[0] = 1
m = 1000000007
dp[1] = (n * (n-1)) % m
memf = []
mfappend = memf.append
for x in memfact(n,m):
    mfappend(x)
for i in range(2,min(k+1,n)):
    dp[i] = (dp[i-1]+comb(n,i,m)*comb(n-1,i,m)) % m
print((dp[min(n-1,k)]+1)%m)