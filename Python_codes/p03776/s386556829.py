def comb(x,y):
  s = 1
  for i in range(y):
    s = s*(x-i)//(i+1)
  return s

n,a,b = map(int,input().split())
v = list(map(int,input().split()))
v.sort(reverse = 1)

m = v[a-1]
l = -1
while v[l+1] > m:
  l += 1
r = a-1
while r+1 <= n-1 and v[r+1] == m:
  r += 1
#print(l,r)
print(sum(v[:a])/a)
ans = 0
if l == -1:
  for k in range(a,b+1):
    ans += comb(r-l,(k-1-l))
else:
  ans += comb(r-l,(a-1-l))
print(ans)
#print(comb(1,1))