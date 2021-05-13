import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
if a[0]!=0:
    print(-1)
    exit()

ans=0
for i in range(1,n):
    if a[i]>a[i-1]+1:
        print(-1)
        exit()
    if a[i]<=a[i-1]:
        ans+=a[i-1]
ans+=a[n-1]

print(ans)
