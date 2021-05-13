N, M = map(int,input().split())
ab = [list(map(int,input().split())) for n in range(N)]
ab.sort()
ans = 0
for n in range(N):
    if M > ab[n][1]:
        ans += ab[n][0] * ab[n][1]
        M -= ab[n][1]
    else:
        ans += ab[n][0] * M
        print(ans)
        exit()