from sys import stdin
input = stdin.readline

n,t=map(int, input().split())
ti=list(map(int, input().split()))

ans=0
for i in range(1,n):
    if ti[i]-ti[i-1]>=t:
        ans+=t
    else:
        ans+=(ti[i]-ti[i-1])
ans+=t
print(ans)
