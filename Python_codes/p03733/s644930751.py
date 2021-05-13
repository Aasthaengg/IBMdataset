import sys
input=sys.stdin.readline

n,T=map(int,input().split())
t=[int(i) for i in input().split()]
ans=0
for i in range(1,n):
    ans+=min(T,t[i]-t[i-1])
print(ans+T)