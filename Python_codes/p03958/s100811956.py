import sys

k,n=map(int,input().split())
a=list(map(int,input().split()))
if n==1: print(a[0]-1);sys.exit()

a.sort(reverse=True)
ans=max(0,a[0]-1-sum(a[1:]))
print(ans)