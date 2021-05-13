def main():
    from itertools import tee

    S = input()
    it1, it2 = tee(iter(S), 2)
    next(it2)

    ans = 0
    for c1, c2 in zip(it1, it2):
        if c1 != c2: ans += 1
    print(ans)


if __name__ == '__main__':
    main()
