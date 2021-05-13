ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
a=nl()

a = [0]+a+[0]

d=[]

for i in range(n+1):
  d.append(abs(a[i+1]-a[i]))
sa = sum(d)
for i in range(1,n+1):
  print(sa+abs(a[i+1]-a[i-1])-abs(a[i]-a[i-1])-abs(a[i+1]-a[i]))
