def main():
    n, a, b = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    low, high = 0, 1000000000000000000
    while low < high:
        mid = (low + high) // 2
        tmp = 0
        for _h in h:
            if _h > mid * b:
                tmp += (_h - mid * b + a - b - 1) // (a - b)
        if tmp > mid:
            low = mid + 1
        else:
            high = mid
    print(low)


if __name__ == '__main__':
    main()
