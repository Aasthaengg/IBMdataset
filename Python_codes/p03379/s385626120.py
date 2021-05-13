n=int(input())
x=list(map(int,input().split()))
y=sorted(x[:])
l=y[n//2-1]
r=y[n//2]
for xx in x:
  print(l if xx>=r else r)