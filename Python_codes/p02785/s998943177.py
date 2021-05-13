n,k=map(int,input().split())
h=list(map(int,input().split()))
h.sort(reverse=True)
if n-k<=0:
  print(0)
else:
  print(sum(h[k:]))