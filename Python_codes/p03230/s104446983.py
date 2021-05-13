n = int(input())

k = 2
while True:
    t = k * (k - 1) // 2
    if t >= n:
        break
    else:  # t < n
        k += 1

if t == n:
    m = [[None for _ in range(k - 1)] for _ in range(k - 1)]
    v = 1
    for r in range(k - 1):
        for c in range(r + 1):
            m[r][c] = v
            v += 1

    print('Yes')
    print(k)

    for i in range(k - 1):
        s = list()
        for c in range(i + 1):
            s.append(m[i][c])

        cnt = len(s)
        j = 0
        while cnt < k - 1:
            s.append(m[i + 1 + j][i])
            j += 1
            cnt += 1

        s = [k - 1] + s
        print(*s)

    s = list()
    cnt = 0
    j = 0
    while cnt < k - 1:
        s.append(m[j][j])
        j += 1
        cnt += 1

    s = [k - 1] + s
    print(*s)

else:
    print('No')