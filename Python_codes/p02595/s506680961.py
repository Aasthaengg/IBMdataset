n, d = map(int, input().split())
xy = [0]*n
for i in range(n):
  xy[i] = list(map(int, input().split()))
  
def judge(x, y):
  return (((x**2 + y**2)**0.5))

cnt = 0
for i in range(n):
  dis = judge(xy[i][0], xy[i][1])
  if dis <= d:
    cnt += 1
    
print(cnt)