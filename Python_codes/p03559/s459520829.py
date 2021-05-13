from bisect import bisect_left
N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
ans = 0
for b in B:
    ans += bisect_left(A, b) * (N - bisect_left(C, b + 1))
print(ans)