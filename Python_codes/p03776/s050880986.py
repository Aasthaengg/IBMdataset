import math
n,a,b=map(int,input().split())
v=list(map(int,input().split()))
v.sort()
v.reverse()
if a==n:
  print(sum(v)/n)
  print(1)
elif v[a-1]!=v[a]:
  print(sum(v[0:a])/a)
  print(1)
elif v[0]!=v[a-1]:
  print(sum(v[0:a])/a)
  ct1=0;ct2=0
  for i in range(n):
    if v[i]==v[a-1]:
      ct1+=1
      if i<a:
        ct2+=1
  print(math.factorial(ct1)//(math.factorial(ct1-ct2)*math.factorial(ct2)))
else:
  print(sum(v[0:a])/a)
  ct1=0;ans=0
  for i in range(n):
    if v[i]==v[a-1]:
      ct1+=1
  for i in range(a,min(ct1+1,b+1)):
    ans+=math.factorial(ct1)//(math.factorial(ct1-i)*math.factorial(i))
  print(ans)