from math import factorial as f
n=int(input())
m=f(n)
ans=1
p=[1]*1000
for i in range(2,1001):
  while m%i==0:
    m//=i
    p[i]+=1
for i in p:
  ans*=i
  ans%=(10**9+7)
print(ans)