N, K = map(int, input().split())
p = int(1e9+7)
res = 0
d = [0]*K

for i in range(K, 0, -1):
    n = pow(K//i, N, p)

    for j in range(2*i, K+1, i):
        n -= d[j-1]

    d[i-1] = n
    res += n*i
    res %= p

print(res)
