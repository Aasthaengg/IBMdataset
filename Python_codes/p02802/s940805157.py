def resolve():
    n, m = map(int, input().split())
    co = 0
    pe = 0
    P = [0] * n
    for _ in range(m):
        p, s = input().split()
        ind = int(p)-1
        if P[ind] != -1: #既に正解
            if s == "WA":
                P[ind] += 1
            else:
                pe += P[ind]
                P[ind] = -1
                co += 1
    print(co, pe)
resolve()