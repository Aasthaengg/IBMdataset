def resolve():
    n, k = map(int, input().split())
    print(0 if n == 1 or n % k == 0 else 1)


if __name__ == '__main__':
    resolve()
