import bisect
from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(_) for _ in stdin.readline().rstrip().split()]
B = [int(_) for _ in stdin.readline().rstrip().split()]
C = [int(_) for _ in stdin.readline().rstrip().split()]
A.sort()
C.sort()
ans = 0
for b in B:
  ans += bisect.bisect_left(A, b) * (N - bisect.bisect_right(C, b))
print(ans)