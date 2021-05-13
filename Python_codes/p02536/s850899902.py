def main():
    n, m = map(int, input().split())
    uf = [-1] * (n+1)

    def uf_find(a):
        if uf[a]<0:
            uf[a] = a
            return a
        elif uf[a]==a:
            return a
        uf[a] = uf_find(uf[a])
        return uf[a]
    def uf_union(a, b):
        if uf_find(a)==uf_find(b):
            return
        ua, ub = uf_find(a), uf_find(b)
        if ua>ub:
            ua, ub = ub, ua
        uf[ub] = ua
    def uf_leaders():
        return set([uf_find(v) for v in range(1,n+1)])

    for _ in range(m):
        a, b = map(int, input().split())
        uf_union(a, b)

    # print(uf)
    # print(uf_leaders())
    
    ans = len(uf_leaders())-1
    print(ans)

main()