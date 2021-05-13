N, KK = map(int, input().split())
P = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

cnt = [1] * (N+1)
retsu = []
for i in range(1,N+1):
    idx = i
    r = []
    for _ in range(N):
        if cnt[idx] == 0:
            break
        r.append(C[P[idx]])
        cnt[idx] = 0
        idx = P[idx]
    if r:
        retsu.append(r)

ans = -1 * (10 ** 10)
for z in retsu:
    K = KK
    s = sum(z)
    l = len(z)
    if K <= l:
        plus = 0
    elif s <= 0:
        plus = 0
        K = l
    else:
        plus = s * (K // l)
        if K % l == 0:
            plus -= s
    K %= l
    if K == 0:
        K = l
    
    moto = z + z
    point = [[0] * l for _ in range(l+K-1)]
    kari = -1 * (10 ** 10)
    for i in range(l+K-1):
        for j in range(l):
            if i == j:
                point[i][j] = moto[i]
            elif i - j >= K or i < j:
                continue
            else:
                point[i][j] = moto[i] + point[i-1][j]
            kari = max(kari, point[i][j])
    ans = max(ans, plus + kari)
print(ans)