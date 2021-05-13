def main(x: int, y: int):
    award = 0

    if x == y == 1:
        award += 400000

    for i in [x, y]:
        if i == 1:
            award += 300000
        elif i == 2:
            award += 200000
        elif i == 3:
            award += 100000

    print(award)


if __name__ == "__main__":
    x, y = map(int, input().split())

    main(x, y)
