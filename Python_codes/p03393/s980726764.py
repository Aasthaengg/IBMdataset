S=input()
if S=='zyxwvutsrqponmlkjihgfedcba':
  print(-1)
  exit()
alp='abcdefghijklmnopqrstuvwxyz'
N=len(S)
if N<26:
  T=S+alp
  i=0
  while T.index(alp[i])<N:
    i+=1
  print(S+alp[i])
  exit()
  
i=-1
nums=[alp.index(S[i])]
while max(nums)==nums[-1]:
  i-=1
  nums.append(alp.index(S[i]))

out=S[:-len(nums)]
tmp=26
for i in nums[:-1]:
  if i>nums[-1] and tmp>i:
    tmp=i
    
print(out+alp[tmp])
