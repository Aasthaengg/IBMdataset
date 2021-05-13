import sys

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))


a, b, c = rm()
if a == b == c:
  if a & 1:
    print(0)
  else:
    print(-1)
  exit()
cnt = 0
while a & 1 == 0 and b & 1 == 0 and c & 1 == 0:
  a, b, c = (b+c)//2, (a+c)//2, (a+b)//2
  cnt += 1
print(cnt)



