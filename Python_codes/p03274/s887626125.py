def main():
    n, k = list(map(int, input().split()))
    X = list(map(int, input().split()))
    P = []
    M = []
    for x in X:
        if x >= 0:
            P.append(x)
        else:
            M.append(abs(x))
    m_range = [max(0, k - len(P)), min(len(M), k)]
    p_range = [max(0, k - len(M)), min(len(P), k)]
    P = [0, ] + P
    M = [0, ] + M[::-1]
    ans = float('inf')
    for i in range(m_range[0], m_range[1] + 1):
        ans = min(ans, 2 * M[i] + P[k - i])
    for i in range(p_range[0], p_range[1] + 1):
        ans = min(ans, 2 * P[i] + M[k - i])
    print(ans)

if __name__ == '__main__':
    main()
