def main():
    from collections import Counter
    n, m, *abc = map(int, open(0).read().split())
    a = Counter(abc[:n])
    *bc, = zip(*[iter(abc[n:])] * 2)
    bc = sorted(bc, key=lambda x: x[1], reverse=True)
    c = 0
    for i, j in bc:
        a[j] += i
        c += i
        if c > n:
            break

    cnt = n
    ans = 0
    keys = sorted(list(a.keys()), reverse=True)

    for k in keys:
        m = a[k]
        if m <= cnt:
            ans += k * m
            cnt -= m
        else:
            ans += k * cnt
            break

    print(ans)


if __name__ == '__main__':
    main()
