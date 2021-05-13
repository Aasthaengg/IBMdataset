N, M = map(int, input().split())
a = []
maxn = 0
for i in range(N):
    a.append([int(i) for i in input().split()])


maxn = 0
for i in range(8):
    A = []
    tm = [1, 1, 1]
    for j in range(N):
        for k in range(3): # x, y, zの符号決定
            if i & (1 << k):
                tm[k] = a[j][k]
            else:
                tm[k] = -1 * a[j][k]
        A.append(sum(tm))
    A.sort(reverse=True)
    tmp = sum(A[:M])
    maxn = max(maxn, tmp)
print(maxn)