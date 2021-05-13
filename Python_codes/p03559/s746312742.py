n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0
import bisect
for b in B:
    ia = bisect.bisect_left(A, b)
    ic = n-bisect.bisect_right(C, b)
    ans += ia*ic
print(ans)
