N,*f = map(int, open(0).read().split())
F = [f[i*10:i*10+10] for i in range(N)]
P = [f[N*10+i*11:N*10+i*11+11] for i in range(N)]
ans = -1 * pow(10,10)
opened = [0] * 10
for i in range(1,2**10):
    temp = 0
    for j in range(10):
        if i >> j & 1:
            opened[j] = 1
        else:
            opened[j] = 0
    for j in range(N):
        c = sum(opened[k]*F[j][k] for k in range(10))
        temp += P[j][c]
    ans = max(ans,temp)
print(ans)