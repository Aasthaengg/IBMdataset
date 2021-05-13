import sys
S, T = next(sys.stdin).strip().split()
A, B = map(int, next(sys.stdin).split())
U = next(sys.stdin).strip()

if U == S:
  A -= 1
elif U == T:
  B -= 1
else:
  raise ValueError

print(A, B)