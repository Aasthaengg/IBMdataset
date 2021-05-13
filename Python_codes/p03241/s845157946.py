from math import floor
N,M=map(int,input().split())
p= floor(M**0.5)
kumi=[]

for i in range(1,p+1):
  if M%i==0:
    kumi.append((i,M//i))
    
ans=1
for pair in kumi:
  if pair[0]>=N:
    ans = max(ans,pair[1])
  if pair[1]>=N:
    ans = max(ans,pair[0])
print(ans)