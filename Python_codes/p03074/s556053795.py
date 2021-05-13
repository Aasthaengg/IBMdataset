from itertools import *

N,K=map(int,input().split())
S=input()

nums=[]
if S[0]=="0":
  nums.append(0)
i=0
while i<len(S):
  j=i
  while j<len(S) and S[j]==S[i]:
    j+=1
  nums.append(j-i)
  i=j
if S[-1]=="0":
  nums.append(0)

sums=[0]+list(accumulate(nums))

ans=0
for left in range(0,len(sums),2):
  right=left+K*2+1
  if len(sums)<=right:
    right=len(sums)-1
  ans=max(ans,sums[right]-sums[left])

print(ans)
