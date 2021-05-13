def resolve():
    import itertools
    N, M = map(int, input().split())
    S = []
    K = []
    ans = 0
    for _ in range(M):
        s = list(map(int, input().split()))
        K.append(s[0])
        S.append(s[1:])
    P = list(map(int, input().split()))
    for i in itertools.product([0,1], repeat=N):
        count = 0
        for j in range(M):
            ichi = 0
            for q in range(K[j]):
                ichi += i[S[j][q]-1]
            if ichi%2 == P[j]:
                count += 1
        if count == M:
            ans += 1
    print(ans)
resolve()