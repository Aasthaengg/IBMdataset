n,k = map(int, input().split())
ans = 0
for i in range(1,n+1):
  j = i
  b =0
  while j<k:
    j*=2
    b+=1
  ans+=0.5**b
print(ans/n)