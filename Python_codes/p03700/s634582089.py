N,A,B=map(int,input().split())
H=[]
import copy
import math

for i in range(N):
  h=int(input())
  H.append(h)
def isok(k):
  I=H
  I=[i-B*k for i in H]
  count=0
  for i in range(N):
    if I[i]>0:
      count+=math.ceil(I[i]/(A-B))
  if count<=k:
    return True
  else:
    return False

start=0
end=sum(H)//B
while end-start>1:
  mid=(start+end)//2
  if isok(mid):
    end=mid
  else:
    start=mid
print(end)