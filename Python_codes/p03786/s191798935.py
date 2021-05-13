from bisect import bisect_right

N = int(input())
*A, = map(int, input().split())
A.sort()

ac = [0]*(N+1)
for i in range(1, N+1):
    ac[i] = ac[i-1]+A[i-1]
ans = 0
for i in A:
    bef = bisect_right(A, i*2)
    aft = bisect_right(A, ac[bef]*2)
    while bef!=aft:
        v = ac[aft]
        bef = aft
        aft = bisect_right(A, ac[aft]*2)
    ans += int(aft==N)
print(ans)