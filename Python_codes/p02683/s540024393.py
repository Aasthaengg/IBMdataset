n,m,x=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
minc=float("inf")

for i in range(2**n):
  lst=[0]*(m+1)
  for bit in range(n):
    if (i>>bit)&1==1:
      for ii,aa in enumerate(a[bit]):
        lst[ii]+=aa
  if min(lst[1:]) >= x:
    minc=min(minc,lst[0])
    
print(-1 if minc == float("inf") else minc)
      
    
