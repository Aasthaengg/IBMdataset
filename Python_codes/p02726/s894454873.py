N, X, Y = map(int, input().split())

L = [0 for _ in range(N)]
for i in range(1, N):
    for j in range(i+1, N+1):
        l = min(abs(j-i), abs(X-i) + 1 + abs(Y-j))
        L[l] += 1
for l in L[1:]:
    print(l)