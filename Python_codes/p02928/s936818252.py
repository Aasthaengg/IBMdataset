from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from collections import Counter
def solve():
    mod = 10**9+7
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [A[0]]
    fall_in = 0
    for i in range(1,N):
        fall_in += i - bisect_right(B,A[i])
        insort(B,A[i])
    c = Counter(A)
    double = 0
    for v in c.values():
        double += v*(v-1)//2
    fall_out = N*(N-1)//2 - double
    ans = fall_in * K % mod + fall_out * K*(K-1)//2 % mod
    ans %= mod
    return ans
print(solve())