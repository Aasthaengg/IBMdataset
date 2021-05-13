def main():
    r, D, x = map(int, input().split())
    lst = [0] * 11
    lst[0] = x

    for i in range(1, 11):
        lst[i] = r * lst[i - 1] - D

    print(*lst[1:], sep="\n")


if __name__ == "__main__":
    main()
