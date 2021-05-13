# Zalgo
# https://drken1215.hatenablog.com/entry/2019/09/16/014600


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
    s = input()

    ans = 0

    t = ''
    for c in reversed(s):
        t = c + t
        lcp = z_algo(t)
        for d, x in enumerate(lcp):
            ans = max(ans, min(x, d))

    print(ans)


if __name__ == '__main__':
    main()
