def main():
    n = int(input())
    A = list(map(int, input().split()))
    even = sum([a % 2 == 0 for a in A])
    print(pow(3, n) - pow(2, even))


if __name__ == '__main__':
    main()
