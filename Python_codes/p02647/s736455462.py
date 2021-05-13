n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(min(k, 45)):
    b = [0] * n
    for j in range(n):
        mi = max(0, j-a[j])
        ma = min(n-1, j+a[j])
        b[mi] += 1
        if ma + 1 <= n -1:
            b[ma+1] -= 1
    c = [0] * n
    s = 0
    for k in range(n):
        s += b[k]
        c[k] = s
    a = c

for i in a:
    print(i, end=' ')