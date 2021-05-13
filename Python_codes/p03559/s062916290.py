from bisect import bisect_left, bisect_right


N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
ans = 0
for b in B:
    a_upperbound = bisect_left(A, b)
    c_lowerbound = bisect_right(C, b)
    ans += a_upperbound * (N - c_lowerbound)
print(ans)
