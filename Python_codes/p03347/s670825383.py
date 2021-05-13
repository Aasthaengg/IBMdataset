N = int(input())
A = [int(input()) for _ in range(N)]
X = [0] * N

if A[0] > 0:
    print(-1)
    exit()

ans = 0
for i in range(1, N):
    if A[i] - 1 == A[i - 1]:
        ans += 1
    elif A[i] - 1 > A[i - 1]:
        print(-1)
        exit()
    else:
        ans += A[i]
print(ans)