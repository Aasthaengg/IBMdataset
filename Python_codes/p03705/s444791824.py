def main():
    n, a, b = list(map(int, input().split()))
    if (n == 1 and a != b) or (b < a):
        print(0)
        exit()
    mini = a * (n - 1) + b
    maxi = a + b * (n - 1)
    print(maxi - mini + 1)


if __name__ == '__main__':
    main()
