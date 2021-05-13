n= int(input())
if n == 1:
  print(1)
  exit()
ab = [list(map(int,input().split())) for _ in range(n)]
pq = {}
for i in range(n-1):
  for j in range(i+1,n):
    a1,b1 = ab[i]
    a2,b2 = ab[j]
    p = a1-a2
    q = b1-b2
    if p<0 or p==0 and q<0:
      p = -p
      q = -q
    if (p,q) in pq:
      pq[(p,q)] += 1
    else:
      pq[(p,q)] = 1
print(n-max(pq.values()))