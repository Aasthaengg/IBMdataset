import math
n,k=map(int,input().split())
p=0
for i in range(1,n+1):
  if k/i<=1:
    p+=1
  else:
    thrw=math.ceil(math.log2(k/i))
    p+=0.5**thrw
print(p/n)