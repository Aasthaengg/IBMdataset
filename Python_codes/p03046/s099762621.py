
M, K = map(int, input().split())

if M == 0 and K == 0:
    print(0, 0)
elif M == 1 and K == 0:
    print(0, 0, 1, 1)
elif M >= 2 and K < 2 ** M:
    tmp = []
    for n in range(2 ** M):
        if n != K:
            tmp.append(n)
    print(*tmp, K, *tmp[::-1], K)
else:
    print(-1)
