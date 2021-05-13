import sys
input = sys.stdin.readline
cur = -1
c = 0
for i in range(int(input())):
  pre,cur = cur,int(input())
  if cur == 0:
    continue
  elif cur == pre + 1:
    c += 1
  elif cur <= pre:
    c += cur
  else:
    print(-1)
    exit()
print(c)