def main():
    l, r, d = map(int, input().split())

    count = 0
    for i in range(l, r+1):
        if i % d == 0:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
