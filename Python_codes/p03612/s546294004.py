def main():
    n, *p = map(int, open(0).read().split())
    ans = 0
    i = False
    for p, q in enumerate(p, 1):
        j = p == q
        i = (i or j) and (not i)
        ans += i

    print(ans)


if __name__ == '__main__':
    main()
