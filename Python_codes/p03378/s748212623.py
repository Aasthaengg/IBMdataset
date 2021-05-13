n,m,x = map(int,input().split())
a = list(map(int,input().split()))

c1 = [i for i in range(x)]
c2 = [i for i in range(x,n+1)]
y=0
z=0
for i in c1:
  if i in a:
    y += 1
for i in c2:
  if i in a:
    z += 1
print(min(y,z))