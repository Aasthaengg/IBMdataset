prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
num = [0 for i in range(len(prime))]
n = int(input())
vec = [i for i in range(1,n+1)]
for i in vec:
  while i>1:
    for j in range(len(prime)):
      if i%prime[j]==0:
        num[j]+=1
        i//=prime[j]
ans=0
for i in range(len(num)):
  for j in range(i+1,len(num)):
    for k in range(len(num)):
      if i==k or j==k:
        continue
      if num[i]>=4 and num[j]>=4 and num[k]>=2:
        #print(prime[i],prime[j],prime[k])
        ans+=1
for i in range(len(num)):
  for j in range(len(num)):
    if i==j:
      continue
    if num[i]>=24 and num[j]>=2:
      ans+=1
    if num[i]>=14 and num[j]>=4:
      ans+=1    
for i in range(len(num)):
  if num[i]>=74:
    ans+=1
print(ans)