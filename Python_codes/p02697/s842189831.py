N, M = map(int, input().split())
X = [0 for _ in range(N)]
if N % 2 == 0:
    X = [0 for _ in range((N-1)//2)]
    l, r = 1, N // 2
    for i in range((N//2)//2):
        X[i] = [l, r]
        l += 1
        r -= 1
    l, r = N, N // 2 + 2
    for i in range((N-1)//2-(N//2)//2):
        X[i+(N//2)//2] = [l, r]
        l -= 1
        r += 1
    for i in range(M):
        print(X[i][0], X[i][1])
else:
    for i in range(M):
        print(N-i, i+1)
