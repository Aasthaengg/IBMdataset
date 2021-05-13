n=int(input())
l=list(map(int,input().split()))
x=sorted(l)
m=(x[n//2]+x[n//2-1])/2
for y in l:
  if y<m:
    print(x[n//2])
  else:
    print(x[n//2-1])