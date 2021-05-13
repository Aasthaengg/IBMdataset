from bisect import bisect_right, bisect_left
N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())
A.sort()
B.sort()
C.sort()
lc = len(C)
ans = 0
for b in B:
    a = bisect_left(A, b)
    c = len(C) - bisect_right(C, b)
    ans += a * c
print(ans)
