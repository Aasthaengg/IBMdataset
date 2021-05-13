W, H, N = map(int, input().split())
A = [0, W, 0, H]
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        A[0] = max(A[0], x)
    elif a == 2:
        A[1] = min(A[1], x)
    elif a == 3:
        A[2] = max(A[2], y)
    else:
        A[3] = min(A[3], y)
a = A[1] - A[0]
b = A[3] - A[2]
if a >= 0 and b >= 0:
    ans = a * b
else:
    ans = 0
print(ans)