def main():
    from bisect import bisect_left as bl
    a, b, q, *stx = map(int, open(0).read().split())
    s = [-float('Inf')] + stx[:a] + [float('Inf')]
    t = [-float('Inf')] + stx[a:a + b] + [float('Inf')]
    x = stx[a + b:]
    tmp = []
    for i in x:
        f, g = bl(s, i), bl(t, i)

        sr, sl = s[f - 1], s[f]
        tr, tl = t[g - 1], t[g]

        d = min([max(sl, tl) - i, i - min(sr, tr), 2 * (tl - sr) - max(i - sr, tl - i), 2 * (sl - tr) - max(sl - i, i - tr)])
        tmp.append(d)

    ans = '\n'.join(map(str, tmp))
    print(ans)


if __name__ == '__main__':
    main()
