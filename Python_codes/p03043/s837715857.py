N, K = map(int, input().split())
p = 0.0
for i in range(1, N+1):
    pp = 1 / N
    x = i
    while (x < K):
        pp /= 2
        x *= 2
    p += pp
print(p)