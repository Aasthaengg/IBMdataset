import numpy as np
n=int(input())
a=list(map(int,input().split()))+[10**6+1]
a=sorted(a)
flag=np.array([0 for i in range(10**6+1)])
ans=0
for i in range(n):
    if flag[a[i]]==0:
        flag[::a[i]]=1
        if a[i]!=a[i+1]:
            ans+=1
print(ans)