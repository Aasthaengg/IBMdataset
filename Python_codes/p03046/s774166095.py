M, K = map(int, input().split())

if M == 1:
    if K == 0:
        print("1 1 0 0")
    else:
        print(-1)
elif 2**M > K:
    X = list(range(K)) + list(range(K+1, 2**M))
    ans = " ".join(map(str, X + [K] + X[::-1] + [K]))
    print(ans)
else:
    print(-1)