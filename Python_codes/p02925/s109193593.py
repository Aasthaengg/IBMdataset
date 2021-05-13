def main():
    N = int(input())
    A = [list(reversed(list(map(lambda x: int(x) - 1, input().split())))) for _ in range(N)]
    d = 0
    r = N
    cur = list(range(N))
    w = [a.pop() for a in A]
    while r:
        d += 1
        nxt = []
        for i in cur:
            o = w[i]
            if o == -1:
                continue
            if w[o] == i:
                nxt.append(i)
                nxt.append(o)
                w[i] = -1
                w[o] = -1
        if not nxt:
            return -1
        cur = []
        for i in nxt:
            if A[i]:
                w[i] = A[i].pop()
                cur.append(i)
            else:
                r -= 1
    return d


print(main())
