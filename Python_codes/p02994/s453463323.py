n,l = map(int, input().split())
a = 200
ans=0
for i in range(l,l+n):
  ans+=i
  if abs(i) < abs(a):
    a = i
print(ans-a)