n,k=map(int,input().split())
h=list(map(int,input().split()))
h.sort(reverse=True)
if n<=k:
  print(0)
  exit()
  
for i in range(k):
  h[i]=0
print(sum(h))