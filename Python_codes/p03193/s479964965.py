def main():
    n, h, w = [int(i) for i in input().split()]
    # print(n, h, w)
    # alloys = []
    count = 0
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        if a >= h and b >= w:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
