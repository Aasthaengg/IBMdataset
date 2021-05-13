n,k,q = map(int,input().split())
pts = [0]*(n+1)
for _ in range(q):
  a = int(input())
  pts[a] += 1
ans = [k+a-q for a in pts]
for v in ans[1:]:
  print('Yes' if v>0 else 'No')