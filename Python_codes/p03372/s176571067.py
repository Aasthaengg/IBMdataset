#AC dattakedo segtree iranaikara keshita
def main():
    N, C = map(int, input().split())
    S = []
    for i in range(N):
        x, v = map(int, input().split())
        S.append((x,v))
    r = [S[0][1] - S[0][0]]
    rm = [S[0][1] - S[0][0]]
    for i, v in enumerate(S[1:], start=1):
        r.append(r[-1] + v[1] - (v[0] - S[i-1][0]))
        rm.append(max(rm[-1], r[-1]))
    l = [S[-1][1] + S[-1][0] - C]
    lm = [S[-1][1] + S[-1][0] - C]
    for i, v in enumerate(reversed(S[:-1]), start=1):
        l.append(l[-1] + v[1] - (S[N-i][0] - v[0]))
        lm.append(max(lm[-1], l[-1]))
    l.reverse()
    lm.reverse()
    m = 0
    for i in range(N):
        rr = r[i] - S[i][0] + lm[i+1] if i < N-1 else 0
        ll = l[i] + S[i][0] - C + rm[i-1] if i > 0 else 0
        m = max(m, r[i], rr, ll, l[i])
    return m
print(main())
