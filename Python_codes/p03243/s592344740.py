import sys
N = int(input())
for i in range(0,112):
  n = list(str(N+i))
  if n[0] == n[1] == n[2]:
    print(N+i)
    sys.exit()