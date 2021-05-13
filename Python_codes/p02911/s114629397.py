n,k,q=map(int,input().split())
a=[]
for _ in range(q):
  a.append(int(input()))

points = [k]*(n+1)
plus = [0]*(n+1)
for i in range(q):
  plus[a[i]] += 1

for i in range(1,n+1):
  points[i] = points[i] - q + plus[i]
  if points[i] >= 1:
    print('Yes')
  else:
    print('No')
