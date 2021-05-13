N = int(input())
A = [int(input()) for _ in range(N)]
if A[0]:
    print(-1)
    exit()
ans = 0
dp = A[-1]
for i in range(N - 1, 0, -1):
    if A[i - 1] == A[i] - 1:
        continue
    elif A[i - 1] >= A[i]:
        ans += dp
        dp = A[i - 1]
    else:
        print(-1)
        exit()
print(ans + dp)
