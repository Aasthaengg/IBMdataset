import sys
def input():
  return sys.stdin.readline().rstrip()

N=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(N):
  tmp=0
  while a[i]%2==0:
    tmp+=1
    a[i]//=2
  ans+=tmp

print(ans)
