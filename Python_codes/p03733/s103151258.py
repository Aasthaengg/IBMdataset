N,T = map(int,input().split())
t = list(map(int,input().split()))
x = T
for i in range(N-1):
  j= t[i+1]-t[i]
  if j>=T:
      x += T
  else:
      x += j
print(x)