import numpy as np
def main():
    n, k = list(map(int, input().split()))
    S = list(input())
    T = []
    V = []
    a, c = S[0], 0
    for s in S:
        if s == a:
            c += 1
        else:
            T.append(a)
            V.append(c)
            a = s
            c = 1
    T.append(a)
    V.append(c)

    V = np.cumsum(np.array(V))
    max_v = len(V)
    ans = 0
    for i, t in enumerate(np.array(T)):
        if t == '0':
            r = i + 2 * k - 1
        else:
            r = i + 2 * k
        if i == 0:
            ans = max(ans, V[min(max_v - 1, r)])
        else:
            ans = max(ans, V[min(max_v - 1, r)] - V[i - 1])
    print(ans)


if __name__ == '__main__':
    main()
