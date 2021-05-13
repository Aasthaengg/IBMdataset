def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    if n == len(set(a)):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
