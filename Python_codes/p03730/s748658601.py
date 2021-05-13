def main():
    a, b, c = map(int, input().split())
    for num in range(a, 50000, a):
        if num % b == c:
            print('YES')
            return

    print('NO')

if __name__ == "__main__":
    main()
