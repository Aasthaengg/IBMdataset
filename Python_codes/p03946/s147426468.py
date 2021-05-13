import sys
input = sys.stdin.readline
n,t=map(int,input().split())
a=list(map(int,input().split()))
m=a[0]
M=0
for i in range(1,n):
    m=min(m,a[i-1])
    M=max(M,a[i]-m)
m=a[0]
ans=0
for i in range(1,n):
    m=min(m,a[i-1])
    if a[i]-m==M:
        ans+=1
print(ans)
