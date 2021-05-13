L, R = map(int, input().split())
a=[]

if R-L>=2019:
  ans=0
else:
  l, r = L%2019, R%2019
  ans=2018**2
  for i in range(l,r):
    for j in range(l+1,r+1):
        k = (i*j) % 2019
        ans = min(ans,k)
print(ans)