import sys
N = int(next(sys.stdin))
A = tuple(map(int, next(sys.stdin).strip().split()))
a = frozenset(A)

print('YES' if len(A) == len(a) else 'NO')