N = int(input())

F = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    v = 0
    for i in range(5 * 2):
        v += tmp[i] << i
    F.append(v)

P = []
for _ in range(N):
    p = list(map(int, input().split()))
    P.append(p)

ans = -1 * (10**12)
for bit in range(1, 1 << (5 * 2)):
    v = 0
    for i in range(len(F)):
        f = F[i]
        product = bit & f
        cnt = 0
        for j in range(5 * 2):
            if product & (1 << j):
                cnt += 1
        v += P[i][cnt]
    ans = max(ans, v)
print(ans)
