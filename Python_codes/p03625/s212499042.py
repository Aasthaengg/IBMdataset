def main():
    from collections import Counter
    n, *a = map(int, open(0).read().split())
    b = Counter(a)
    *c, = map(lambda x: tuple(x), b.items())
    c.sort(key=lambda x: x[0], reverse=True)

    ans = 1
    count = 0
    for (k, v) in c:
        if v >= 4 and ans == 1:
            ans = k ** 2
            count += 2
            break
        if v >= 2:
            ans *= k
            count += 1
        if count == 2:
            break
    if count < 2:
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    main()
