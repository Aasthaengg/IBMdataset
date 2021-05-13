def main() -> None:
    n, k = map(int, input().split())

    check = [0] * n
    for _ in range(k):
        _ = input()
        having = tuple(map(int, input().split()))
        for idx in having:
            check[idx-1] += 1
    print(check.count(0))
    return


if __name__ == '__main__':
    main()
