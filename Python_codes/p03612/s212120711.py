def main():
    n, *p = map(int, open(0).read().split())
    res = []
    tmp = False
    for i, j in enumerate(p, 1):
        if i == j:
            tmp = not tmp
            res.append(tmp)
        else:
            tmp = False

    ans = sum(res)
    print(ans)


if __name__ == '__main__':
    main()
