n,m=map(int,input().split())
low=1
high=n 
for _ in range(m):
    l,r=map(int,input().split())
    low=max(l,low)
    high=min(r,high)
if high-low+1>=0:
    print(high-low+1)
else:
  print(0)