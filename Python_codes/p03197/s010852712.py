import sys


N, *A = map(int, open(0).read().split())

for a in A:
  if a % 2:
    print("first")
    sys.exit()
  
print("second")