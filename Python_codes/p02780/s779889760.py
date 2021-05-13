n,k=map(int, input().split())
p=[0]+list(map(int, input().split()))

from itertools import accumulate
acc = list(accumulate(p))

ans = 0
for st in range(n-k+1):
    ans=max(acc[k+st]-acc[st],ans)
    
print((ans+k)/2)