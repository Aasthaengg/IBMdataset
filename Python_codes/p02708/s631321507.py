import numpy as np

n, k = map(int, input().split())
#print(n,k)
ary = np.array([i for i in range(n+1)])
cum = np.cumsum(ary)
#print(cum)

ans = 0
for j in range(k,n+1):
    ans += (cum[-1] - cum[-j-1]) - cum[j-1] + 1
    
else:
    ans += 1
    ans %= 10**9+7

print(ans)