def ALDS1_3B():
    n, q = map(int, input().split())
    PQ = [[l[0], int(l[1])] for l in  [input().split() for i in range(n)]  ]
    times = 0
    while PQ:
        p = PQ.pop(0)
        if p[1] <= q:
            times += p[1]
            print('%s %d' %(p[0], times))
        else:
            times += q
            PQ.append([p[0], p[1]-q])


if __name__ == '__main__':
    ALDS1_3B()