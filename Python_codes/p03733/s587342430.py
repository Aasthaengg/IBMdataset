import sys
input=sys.stdin.readline

n,T=map(int,input().split())
t=list(map(int,input().split()))
res=0
for i in range(n-1):
    if t[i]+T>t[i+1]:
        res+=(t[i+1]-t[i])
    else:
        res+=T
res+=T
print(res)