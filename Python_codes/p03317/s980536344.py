def main():
    n, k = map(int, input().split())
    a_lst = list(map(int, input().split()))

    tmp = k
    count = 1
    while tmp < n:
        tmp += k - 1
        count += 1

    print(count)


if __name__ == '__main__':
    main()