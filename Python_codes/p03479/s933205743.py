import sys
x,y = map(int,input().split())
cnt = 1
for i in range(1,100):
  if x*2 <= y:
    cnt += 1
    x *= 2
  else:
    print(cnt)
    sys.exit()