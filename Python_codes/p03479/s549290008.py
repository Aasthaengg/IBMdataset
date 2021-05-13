x,y = list(map(int,input().split()))

n = x
cnt = 0
while n <= y:
  n = n*2
  cnt += 1

print(cnt)