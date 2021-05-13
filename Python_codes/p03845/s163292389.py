n = int(input())
t = tuple(map(int,input().split()))
m = int(input())
px = [tuple(map(int,input().split())) for _ in range(m)]

s = sum(t)
for i in range(m):
  p,x = px[i]
  p -= 1
  print(s-t[p]+x)