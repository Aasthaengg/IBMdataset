M, K = map(int, input().split())
if 2**M <= K:
    print(-1)
    exit(0)
if M == 1:
    if K == 1:
        print(-1)
    else:
        print("0 0 1 1")
else:
    R = [i for i in range(2**M) if i != K]
    *S, = reversed(R)
    ans = [K] + R + [K] + S
    print(*ans)
