modx=10**9+7
n=int(input())
p=1
for i in range(1,n+1):
  p=p*i %modx
print(p)