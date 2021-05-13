M,K= map(int,input().split())

if K >= 2**M:
    print(-1)
    exit()

if M == 0:
    print("0 0")
    exit()

if M == 1:
    if K == 0:
        print("0 0 1 1")
    if K == 1:
        print(-1)
    exit()

left = [i for i in range(2**M) if not i == K]

ans = left + [K] + left[::-1] + [K]

print(*ans)


