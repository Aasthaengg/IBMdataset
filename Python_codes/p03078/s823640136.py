from bisect import bisect_left
import sys
input=sys.stdin.readline
x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
bc=[]
for i in b:
  for j in c:
    bc.append(i+j)
bc.sort()
yz=y*z
ng=10**12
ok=1
while ng-ok>1:
  mid=(ok+ng)//2
  cnt=0
  for j in a:
    cnt+=yz-bisect_left(bc,mid-j)
  #print(cnt)
  if cnt>=k:
    ok=mid
  else:
    ng=mid
ans=[]
#print(ok)
for i in a:
  idx=bisect_left(bc,ok-i)
  for j in range(idx,yz):
    ans.append(i+bc[j])
ans.sort(reverse=True)
#print(len(ans))
for i in ans[:k]:
  print(i)