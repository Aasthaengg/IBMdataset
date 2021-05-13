import sys
import bisect

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()
C.sort()
# print(A)
# print(B)
# print(C)
ans = 0
for i in range(N):
    mid = B[i]
    top = bisect.bisect_left(A, mid)
    down = bisect.bisect_right(C, mid)
    # print(top, down)
    ans += top * (N - down)

print(ans)