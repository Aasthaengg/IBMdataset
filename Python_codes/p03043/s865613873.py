import math

n, k  = map(int, input().split())
if k<=n:
    ans = 0
    for i in range(1, k):
        m = math.ceil(math.log2(k/i))
        ans+=1/pow(2, m)
    ans/=n
    ans += (n-k+1)/n
    print(ans)
else:
    ans = 0
    for i in range(1, n+1):
        m = math.ceil(math.log2(k/i))
        ans+=1/pow(2, m)
    ans/=n
    print(ans)