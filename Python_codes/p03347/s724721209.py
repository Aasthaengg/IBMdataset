N = int(input())
A = [int(input()) for _ in range(N)]
if 0 < A[0]:
    print(-1)
    exit()
ans = 0
for i in range(1, N):
    if 1 < A[i] - A[i - 1]:
        print(-1)
        exit()
    elif A[i] - A[i - 1] == 1:
        ans += 1
    elif A[i] == A[i - 1]:
        ans += A[i]
    else:
        ans += A[i]
print(ans)