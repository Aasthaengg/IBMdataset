n,k = map(int, input().split())
a = []
for i in range(1,n+1):
  j = i
  b =0
  while j<k:
    j*=2
    b+=1
  a.append(b)
ans = 0
for i in range(n):
  ans+=0.5**a[i]
print(ans/n)