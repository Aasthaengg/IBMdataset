def main():
    cakes, variation = map(int, input().split())
    cake_num = list(map(int, input().split()))
    cake_num.sort()
    print(max(0, 2 * cake_num[-1] - cakes - 1))


if __name__ == '__main__':
    main()

