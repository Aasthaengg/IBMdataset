def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if not a in d:
            d[a] = 1
        else:
            d[a] += 1
    tup = sorted([(k, v) for k, v in d.items() if v > 1], key=lambda x: x[0])
    #print(tup)
    hd = []
    while len(tup) > 0:
        length, cnt = tup.pop()
        if cnt >= 4:
            hd.append(length)
        if cnt >= 2:
            hd.append(length)
        if len(hd) >= 2:
            print(hd[0]*hd[1])
            return
    print(0)




if '__main__' == __name__:
    resolve()