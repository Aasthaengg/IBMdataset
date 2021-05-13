n,k,q = map(int,input().split())
pts = [0]*(n+1)
for _ in range(q):
  a = int(input())
  pts[a] += 1
for v in pts[1:]:
  print('Yes' if v+k-q>0 else 'No')