def main():
    a, b, x = map(int, input().split())

    if x > a + b or a > x:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()