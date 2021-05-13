import bisect

n = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
ans = 0
L = [0] * n
for i in range(n):
    a = bisect.bisect_left(A, B[i])
    L[i] = a
cum = [0] * (n + 1)
for i in range(n):
    cum[i+1] = cum[i] + L[i]
for i in range(n):
    b = bisect.bisect_left(B, C[i])
    ans += cum[b]
print(ans)
