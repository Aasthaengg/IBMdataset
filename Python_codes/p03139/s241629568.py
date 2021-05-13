def main():
    n, a, b = list(map(int, input().split()))
    print(min(a, b), max(a + b - n, 0))

if __name__ == '__main__':
    main()
