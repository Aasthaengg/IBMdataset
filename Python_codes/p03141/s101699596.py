N = int(input())
A = [0] * N

ans = 0
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a + b
    ans -= b
A = sorted(A, reverse=True)
for i in range(N):
    if i % 2 == 0:
        ans += A[i]
print(ans)
