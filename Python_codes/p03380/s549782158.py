n=int(input())
a=sorted(list(map(int,input().split())))
l=a[-1]
b=[abs(i-l/2) for i in a]
c=float("inf")
for i in range(n-1):
  c=min(c,b[i])
print(l,a[b.index(c)])