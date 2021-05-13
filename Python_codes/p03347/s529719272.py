import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for i in range(n)]
cur = -1
c = 0
for i in a:
  pre,cur = cur,i
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