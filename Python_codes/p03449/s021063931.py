N = int(input())
A = [0] * 2
A[0] = list(map(int, input().split()))
A[1] = list(map(int, input().split()))

ans = 0
for i in range(N):
    now = 0
    for j in range(N):
        if j < i:
            now += A[0][j]
        elif j > i:
            now += A[1][j]
        else:
            now += A[0][j] + A[1][j]
    ans = max(ans, now)
print(ans)