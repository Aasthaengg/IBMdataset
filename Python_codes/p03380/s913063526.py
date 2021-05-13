N = int(input())
*A, = map(int, input().split())
A.sort()
m = A[-1]
x = m / 2
ans = A[0]
for i in range(1, N-1):
    if abs(ans - x) > abs(A[i] - x):
        ans = A[i]
print(m, ans)