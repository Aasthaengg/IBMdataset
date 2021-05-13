def main():
    from collections import Counter
    n, m, *abc = map(int, open(0).read().split())
    a = Counter(abc[:n])
    bc = abc[n:]
    for i, j in zip(*[iter(bc)] * 2):
        a[j] += i

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
