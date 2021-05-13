def main():
    a, b, c = map(int, input().split())
    cond = b * 2 == a + c
    print('YES' if cond else 'NO')


if __name__ == '__main__':
    main()
