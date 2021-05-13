def main():
    n = int(input())
    # n, k = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()

    count = 0
    for i in range(1, n+1):
        i = str(i)
        if len(i) % 2 != 0:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
