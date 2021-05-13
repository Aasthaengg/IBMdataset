import sys
N, D = map(int,input().split())
count = 0
for s in sys.stdin.readlines():
   X, Y = map(int, s.split())
   if X**2+Y**2 <= D**2:
      count += 1
print(count)