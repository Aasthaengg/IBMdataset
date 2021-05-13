import sys

n = int(input())
a = map(int, input().split())
ans = sys.maxsize
for an in a:
  cnt = 0
  while an % 2 == 0:
    an /= 2
    cnt += 1
  if cnt < ans:
    ans = cnt
print(ans)