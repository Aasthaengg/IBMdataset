if __name__ == '__main__':
    a, b, c = map(int, input().split())

    for i in range(1000000):
        m = a * i % b
        if m == c:
            print('YES')
            exit(0)
    print('NO')