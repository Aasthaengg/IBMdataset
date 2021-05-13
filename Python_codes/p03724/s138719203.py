import numpy as np
n,m=map(int,input().split())
s=np.zeros(n+1)
for i in range(m):
    a,b=map(int,input().split())
    s[a]+=1
    s[b]+=1
print("NO" if sum(s%2)else"YES")