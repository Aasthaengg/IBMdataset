N,M=map(int,input().split())
l=list(map(int,input().split()))
total=0
for k in range(M):
  total+=l[k]
if total<=N:
  print(N-total)
else:
  print("-1")