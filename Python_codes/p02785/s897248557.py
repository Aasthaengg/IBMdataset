n,k,*h=map(int,open(0).read().split())
if k>=n:
  print(0)
  exit()
h.sort(reverse=True)
for i in range(k):
  h[i]=0
print(sum(h))