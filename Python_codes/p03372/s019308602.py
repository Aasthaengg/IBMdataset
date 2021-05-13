def solve():
    N,C = map(int,input().split())
    x = [0 for i in range(N)]
    v = [0 for i in range(N)]
    for i in range(N):
        x[i],v[i] = map(int,input().split())

    sc = 0
    v11 = [0 for i in range(N)]
    v12 = [0 for i in range(N)]
    for i in range(N):
        sc += v[i]
        v11[i] = sc - x[i]
        v12[i] = sc - x[i] * 2
    for i in range(1,N):
        v11[i] = max(v11[i], v11[i-1])
        v12[i] = max(v12[i], v12[i-1])

    sc = 0
    v21 = [0 for i in range(N)]
    v22 = [0 for i in range(N)]
    for i in range(N-1,-1,-1):
        sc += v[i]
        v21[i] = sc - (C - x[i])
        v22[i] = sc - (C - x[i]) * 2
    for i in range(N-2,-1,-1):
        v21[i] = max(v21[i], v21[i+1])
        v22[i] = max(v22[i], v22[i+1])

    ans = 0
    for i in range(N):
        ans = max(ans, v11[i])
        ans = max(ans, v21[i])
    for i in range(N-1):
        ans = max(ans, v12[i]+v21[i+1])
        ans = max(ans, v11[i]+v22[i+1])

    return ans

print(solve())
