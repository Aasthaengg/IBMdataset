def main(n: int, a: list):
    prev = [0, 0]
    ans = 0

    for _a in a:
        if _a == prev[0]:
            if prev[1] % 2 == 0:
                ans += 1

            prev[1] += 1
        else:
            prev = [_a, 0]

    print(ans)


if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())

    main(n, a)
