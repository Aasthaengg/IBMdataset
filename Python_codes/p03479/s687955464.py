x,y = map(int,input().split())
tmp = x
cnt = 0

while tmp <= y:
  tmp *= 2
  cnt += 1

print(cnt)