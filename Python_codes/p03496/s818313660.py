N = int(input())
A = list(map(int, input().split()))

M, X, Xi = 0, 0, 1
for i, a in enumerate(A, start=1):
    if abs(a) > M:
        M = abs(a)
        X = a
        Xi = i

if X > 0:
    ans = []
    for i in range(N):
        A[i] += X
        ans.append((Xi, i + 1))

    for i in range(N - 1):
        A[i + 1] += A[i]
        ans.append((i + 1, i + 2))

    print(len(ans))
    for x, y in ans:
        print(x, y)

else:
    ans = []
    for i in range(N):
        A[i] += X
        ans.append((Xi, i + 1))

    for i in range(N - 1, 0, -1):
        A[i - 1] += A[i]
        ans.append((i + 1, i))

    print(len(ans))
    for x, y in ans:
        print(x, y)
