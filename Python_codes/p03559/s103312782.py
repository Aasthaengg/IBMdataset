import bisect

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()
LC = len(C)
ans = 0
for b in B:
    na = bisect.bisect_left(A, b)
    nc = LC - bisect.bisect_right(C, b)
    ans += na * nc

print(ans)