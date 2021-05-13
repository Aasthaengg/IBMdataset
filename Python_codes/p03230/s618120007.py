n = int(input())

for k in range(1000):
    temp = k * (k - 1) // 2
    if n == temp:
        print('Yes')
        print(k)
        res = [[] for _ in range(k)]
        p = 1
        for i in range(k):
            for j in range(i + 1, k):
                res[i].append(p)
                res[j].append(p)
                p += 1
        for x in res:
            print(' '.join(map(str, [k - 1] + x)))
        break
    elif n < temp:
        print('No')
        break