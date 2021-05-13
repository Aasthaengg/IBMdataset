import sys
readline = sys.stdin.readline

L,R = map(int,readline().split())

if abs(R - L) >= 2019:
  print(0)
  exit(0)
  
L %= 2019
R %= 2019

if L > R:
  L,R = R,L

if L == R:
  print(0)
  exit(0)

ans = 2019
for i in range(L, R):
  for j in range(i + 1, R + 1):
    if (i * j) % 2019 < ans:
      ans = (i * j) % 2019
      
print(ans)