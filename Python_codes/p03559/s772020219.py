import sys
readline = sys.stdin.readline

N = int(readline())
A = sorted(list(map(int,readline().split())))
B = list(map(int,readline().split()))
C = sorted(list(map(int,readline().split())))

ans = 0
import bisect
for i in range(len(B)):
  ind_a = bisect.bisect_left(A, B[i])
  ind_c = bisect.bisect_right(C, B[i])
  ans += ind_a * (len(C) - ind_c)
  
print(ans)