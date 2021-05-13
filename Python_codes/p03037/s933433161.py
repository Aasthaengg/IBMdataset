n , m = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(m)]

mi = 0
ma = n
for i in range(m):
  mi = max(mi, lr[i][0])
  ma = min(ma, lr[i][1])
  
  
if ma-mi>=0:
  print(ma-mi+1)
else:
  print(0)