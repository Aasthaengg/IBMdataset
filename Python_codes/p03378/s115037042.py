n,m,x = map(int,input().split())
a = list(map(int,input().split()))
up = 0
down = 0
for i in range(x):
  if i in a:
    down += 1
for i in range(x,n):
  if i in a:
    up += 1
print(min(up,down))