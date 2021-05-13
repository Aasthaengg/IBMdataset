N, x = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(N):
    if i == 0:
        B.append(A[i])
    else:
        B.append(A[i]+A[i-1])
B.append(A[-1])

ans = 0
for i in range(N):
    if B[i] > x:
        a = B[i] - x
        ans += a
        B[i] -= a
        B[i+1] -= a
if B[N] > x:
    ans += B[N]-x

print(ans)
