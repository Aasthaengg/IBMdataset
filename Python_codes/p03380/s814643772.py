n=int(input())
a=list(map(int,input().split()))
a.sort()
a.reverse()
x=a[0]
diff=10**9
for i in range(1,n):
  if abs(x-2*a[i])<diff:
    y=a[i]
    diff=abs(x-2*y)
print(x)
print(y)