x = int(input())
cnt = 0
while x>0:
  cnt += 1
  x = max(0,x-cnt)
print(x+cnt)