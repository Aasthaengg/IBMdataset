def main():
    a, b, c = map(int, input().split())
    k = int(input())

    count = 0
    while True:
        if a < b:
            if b < c:
                break
            else:
                c *= 2
                count += 1
        else:
            b *= 2
            count += 1
    print('Yes' if count <= k else 'No')


if __name__ == '__main__':
    main()
