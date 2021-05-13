import sys
n=int(input())
#n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=1
if 0 in a:
  print(0)
  sys.exit()
for i in range(n):
  ans*=a[i]
  if ans>10**18:
    ans=-1
    break
print(ans)