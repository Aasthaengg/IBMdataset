N=int(input())
*A,=map(int, input().split())
*B,=map(int, input().split())
*C,=map(int, input().split())

A.sort()
B.sort()
C.sort()

ans = 0
from bisect import bisect_left, bisect_right
for b in B:
    ac = bisect_left(A,b)
    cc = N - bisect_right(C,b)
    ans += ac * cc
print(ans)