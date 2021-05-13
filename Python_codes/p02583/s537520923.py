def main():
    n = int(input())
    ls = sorted(list(map(int, input().split())))
    ans = 0

    for i, li in enumerate(ls):
        for j, lj in enumerate(ls[i+1:]):
            if li == lj:
                continue
            for lk in ls[i+j+2:]:
                if lj == lk:
                    continue

                if li + lj > lk:
                    ans += 1

    print(ans)


if __name__ == '__main__':
    main()
