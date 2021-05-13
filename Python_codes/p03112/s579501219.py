def main():
    from bisect import bisect_left as bl
    a, b, q, *stx = map(int, open(0).read().split())
    s = [-float('Inf')] + stx[:a] + [float('Inf')]
    t = [-float('Inf')] + stx[a:a + b] + [float('Inf')]
    x = stx[a + b:]
    tmp = []
    for i in x:
        f, g = bl(s, i), bl(t, i)

        sl, sr = s[f - 1], s[f]
        tl, tr = t[g - 1], t[g]

        d = float('Inf')
        for j in [sl, sr]:
            for k in [tr, tl]:
                if j <= i and k <= i:
                    d = min(d, i - min(j, k))
                elif j <= i <= k or k <= i <= j:
                    d = min(d, min(abs(i - j), abs(i - k)) * 2 + max(abs(i - j), abs(i - k)))
                else:
                    d = min(d, max(j, k) - i)

        tmp.append(d)

    ans = '\n'.join(map(str, tmp))
    print(ans)


if __name__ == '__main__':
    main()
