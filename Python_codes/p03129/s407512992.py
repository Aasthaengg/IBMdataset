def main():
    n, k = list(map(int, input().split()))
    print('YES' if k <= -(-n // 2) else 'NO')

if __name__ == '__main__':
    main()
