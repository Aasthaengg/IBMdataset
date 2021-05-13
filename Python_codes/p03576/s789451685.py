N, K = list(map(int, input().split()))
X = [0]*N
Y = [0]*N
for i in range(N):
    X[i], Y[i] = list(map(int, input().split()))
YS = [[Y[i], i] for i in range(N)]
YS.sort()
# print(YS)

ans = 10**20
for i in range(N):
    for j in range(i+1, N):
        l, r = X[i], X[j]
        if l > r:
            l, r = r, l
        u = 0
        d = 0
        A = [(l <= X[k] <= r) for k in range(N)]
        # print(A)
        ct = A[YS[0][1]]
        for d in range(N):
            while ct < K:
                u += 1
                if u >= N:
                    break
                ct += A[YS[u][1]]
                # print(ct)
            else:
                S = (r-l)*(YS[u][0]-YS[d][0])
                ans = min(ans, S)
                ct -= A[YS[d][1]]
print(ans)
