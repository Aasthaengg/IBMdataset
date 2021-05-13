N, K = map(int, input().split())
X = list(map(int, input().split()))
r = -10**18
for i in range(-1, N):
#    print(i)
    for j in range(i+1, N+1):
        A, B = X[:i+1], X[j:]
        if i+1+N-j > K:
            continue
        C = sorted(A+B)[::-1]
#        print(A, B, i+1, N-j, i, j)
        for _ in range(K-(i+1+N-j)):
            if not C:
                break
            c = C.pop()
            if c > 0:
                C.append(c)
                break
        r = max(r, sum(C))
print(r)
