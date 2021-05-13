n,m,x = map(int, input().split())
line = list(map(int, input().split()))
a = 0
b = 0
for i in line:
  if i > x:
    a += 1
  else:
    b += 1
print(min(a,b))