N,K = map(int,input().split())
M = 10 ** 9 + 7
l = [0] * (K + 1)
cnt = 0
for k in range(K,0,-1):
    a = pow(K // k, N, M)
    l[k] = a - sum(l[k*2::k])
for k in range(1,K + 1):
    cnt += k * l[k]
print(cnt % M)
