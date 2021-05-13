import sys
C = list(map(int, input().split()))

res = 0

for c in C:
  if c % 2 == 0:
    print(res)
    sys.exit()

C.sort(reverse=True)

if C[0] % 2 == 0:
  print(0)
else:
  print(C[1] * C[2])