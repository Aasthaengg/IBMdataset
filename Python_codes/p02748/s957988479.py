A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(M)]
ans = min(a) + min(b)
for i in range(M):
    c = a[L[i][0] - 1] + b[L[i][1] - 1] - L[i][2]
    if c < ans:
        ans = c
print(ans)
