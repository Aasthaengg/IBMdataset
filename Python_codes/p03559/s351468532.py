from bisect import bisect_right, bisect_left

N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())

A.sort()
C.sort()
ans = 0

for i in B:
    a = bisect_left(A, i)
    b = N-bisect_right(C, i)
    ans += (a*b)

print(ans)
