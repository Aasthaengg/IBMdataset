N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
now = A[0]
if now > x:
    ans += now - x
    now = x
for i in range(1, N):
    if now + A[i] > x:
        y = now + A[i] - x
        ans += y
        A[i] = max(0, A[i] - y)
    now = A[i]
print(ans)
