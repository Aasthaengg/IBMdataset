a,b,c=map(int,input().split())
cnt = 0
for i in range(a):
  x,y = map(int,input().split())
  if x >= b and y >= c:
    cnt += 1
print(cnt)