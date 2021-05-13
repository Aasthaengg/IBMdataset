L, R = map(int,input().split())

l = L%2019
r = R%2019
ans = 0
if R-L >= 2019:
  ans = 0
else:
  if l>=r:
    ans=0
  else:
    ans = 2018
    for i in range(l,r):
      for j in range(l+1,r+1):
        ans = min(ans, (i*j)%2019)

print(ans)