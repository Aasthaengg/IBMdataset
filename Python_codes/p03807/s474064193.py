def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = sum(x % 2 == 1 for x in a)
    print('YES' if m % 2 == 0 else 'NO')


if __name__ == '__main__':
    main()
