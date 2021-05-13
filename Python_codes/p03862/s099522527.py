N, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    a = A[i - 1]
    b = A[i]
    if a + b <= x:
        continue
    over = (a + b) - x
    ans += over
    A[i] = max(0, b - over)

print (ans)

