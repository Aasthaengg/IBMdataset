N=int(input())
p=1
for i in range(N):
  p*=(i+1)
  p=p%(10**9+7)
print(p)