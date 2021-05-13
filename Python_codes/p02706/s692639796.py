n,m = map(int,input().split())
a = map(int,input().split())

d = n - sum(a)
if d < 0:
  d = -1
print(d)