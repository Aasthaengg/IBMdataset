import math
ans=0
A=[int(input()) for i in range(5)]
a=10
p=0
for i in range(5):
  if a>(A[i]%10) and A[i]%10!=0:
    p=i
    a=A[i]%10
for i in range(5):
  if i==p:
    ans+=A[i]
  else:
    ans+=10*(math.ceil(A[i]/10))
print(ans)