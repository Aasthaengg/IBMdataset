N, M = map(int, input().split())
NUM = 10**9 + 7


if N-1 <= M <= N+1:
    ans = 1
    if N == M:
        for _ in range(2):
            for i in range(1, N+1):
                ans = ans * i % NUM
        ans = ans * 2 % NUM
    else:
        for i in range(1, N+1):
            ans = ans * i % NUM
        for i in range(1, M+1):
            ans = ans * i % NUM
else:
    ans = 0

print(ans)