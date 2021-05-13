n=int(input())
a=[int(x) for x in input().rstrip().split()]
x1=sum(a)-2*sum([a[i] for i in range(1,n-1,2)])
x=[x1]
for i in range(1,n):
  x.append(2*a[i-1]-x[i-1])
print(*x)