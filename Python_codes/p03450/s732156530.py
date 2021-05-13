N, M = map(int, input().split())
T = [[] for _ in range(N+1)]
for _ in range(M):
    L, R, D = map(int, input().split())
    T[L].append((R, D))
    T[R].append((L, -D))
X = [None] * (N + 1)
for i in range(1, N+1):
    if X[i] is not None: continue
    X[i] = 0
    stack = [i]
    while stack:
        L = stack.pop()
        for R, D in T[L]:
            if X[R] is None:
                X[R] = X[L] + D
                stack.append(R)
            else:
                if X[R] - X[L] != D:
                    print("No")
                    exit()
print("Yes")