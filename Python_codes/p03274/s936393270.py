def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    P = []
    M = []
    for x in X:
        if x < 0:
            M.append(-1 * x)
        else:
            P.append(x)
    M.reverse()

    if len(P) == 0:
        print(M[K - 1])
        exit()
    elif len(M) == 0:
        print(P[K - 1])
        exit()

    ans = 10 ** 10
    for i, m in enumerate(M, start=1):
        d = None
        if i == K + 1:
            break
        elif i == K:
            d = m
        else:
            p_idx = K - i - 1
            if p_idx >= len(P):
                continue
            else:
                d = m * 2 + P[p_idx]
        if d < ans:
            ans = d

    for i, p in enumerate(P, start=1):
        d = None
        if i == K + 1:
            break
        elif i == K:
            d = p
        else:
            m_idx = K - i - 1
            if m_idx >= len(M):
                continue
            else:
                d = p * 2 + M[m_idx]
        if d < ans:
            ans = d

    print(ans)


if __name__ == '__main__':
    main()
