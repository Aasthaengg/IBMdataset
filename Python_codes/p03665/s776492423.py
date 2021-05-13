import math
n,p=map(int,input().split())
a=list(map(int,input().split()))
odd=0
even=0
for i in range(n):
  if a[i]%2==0:
    even+=1
  else:
    odd+=1
ans=0
t=1
while t<=odd:
  res=math.factorial(odd)//(math.factorial(t)*math.factorial(odd-t))
  t+=2
  if even!=0:
    w=0
    while w<=even:
      res1=math.factorial(even)//(math.factorial(w)*math.factorial(even-w))
      w+=1
      ans+=res*res1
  else:
    ans+=res
if p==1:
  print(ans)
else:
  print(2**n-ans) 