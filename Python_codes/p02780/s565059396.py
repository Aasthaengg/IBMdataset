import numpy as np
n,k=map(int, input().split())
p=list(map(int,input().split()))


s=[]
p=np.array(p)
sum=0
for i in range(n):
  sum+=(1+p[i])/2
  s.append(sum)
#print(s)
if k==n:
  print(s[-1])
  exit()
max=s[k-1]-s[0]
for j in range(1,n-k):
  #print(j)
  if max<= s[j+k]-s[j]:
    max=s[j+k]-s[j]
  
print(max)