def z_algo(s: str) -> list:
    """LCP(0,i)のlist"""
    N = len(s)
    ret = [-1] * N
    ret[0] = N
    i, j = 1, 0
    while i < N:
        while i + j < N and s[j] == s[i + j]:
            j += 1
        ret[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < N and k + ret[k] < j:
            ret[i + k] = ret[k]
            k += 1
        i += k
        j -= k
    return ret


def main():
    N = int(input())
    S = input()

    ret = 0
    t = ''
    for c in reversed(S):
        t = c + t
        lcp = z_algo(t)
        for diff, len_ in enumerate(lcp):
            ret = max(ret, min(diff, len_))
    print(ret)


if __name__ == '__main__':
    main()
