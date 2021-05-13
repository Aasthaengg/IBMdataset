N = int(input())
A = list(map(int, input().split()))

x = A[0]
y = sum(A[1:])
ans = abs(y - x)
for i in range(1, N - 1):
    x += A[i]
    y -= A[i]
    ans = min(ans, abs(y - x))
print(ans)
