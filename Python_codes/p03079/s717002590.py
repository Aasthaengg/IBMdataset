def main(a, b, c):
    if a == b == c:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    a, b, c = map(int, input().split())

    main(a, b, c)
