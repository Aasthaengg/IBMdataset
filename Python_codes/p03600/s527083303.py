# https://atcoder.jp/contests/abc074/tasks/arc083_b

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

total = 0
for n in range(N):
    for m in range(n + 1, N):
        total += A[n][m]

flag = False
for n in range(N):
    for m in range(n + 1, N):
        for k in range(N):
            if k != n and k != m:
                if A[n][m] > A[n][k] + A[k][m]:
                    flag = True
                    break
                elif A[n][m] == A[n][k] + A[k][m]:
                    # この辺はいらない
                    total -= A[n][m]
                    break
        if total < 0 or flag:
            break
    if total < 0 or flag:
        break

if flag:
    print(-1)
else:
    print(total)