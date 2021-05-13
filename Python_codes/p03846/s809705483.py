import sys
n=int(input())
a=sorted(list(map(int,input().split())))
ans=1
flag=(n+1)%2
if flag==0:
  if a[0]==0:
    a.pop(0)
  else:
    print(0)
    sys.exit()
else:
  if a[0]==a[1]==1:
    a.pop(0)
    a.pop(0)
    ans*=2
  else:
    print(0)
    sys.exit()
for i in range((n-flag-1)//2):
  if a[i*2]==a[i*2+1]==flag+(i+1)*2:
    ans*=2
  else:
    print(0)
    sys.exit()
print(ans%(10**9+7))