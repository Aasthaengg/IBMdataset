def resolve():
    N, M = map(int, input().split())
    K = []
    A = []
    ans = 0
    for _ in range(N):
        a = list(map(int, input().split()))
        K.append(a[0])
        A.append(a[1:])
    for i in range(M):
        count = 0
        for j in range(N):
            if i+1 in A[j]:
                count += 1
        if count == N:
            ans += 1
    print(ans)
resolve()