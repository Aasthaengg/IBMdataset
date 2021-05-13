def main():
    from math import ceil
    n = int(input())
    a, b = 1, 1
    for _ in range(n):
        i, j = map(int, input().split())
        x = max((a + i - 1) // i, (b + j - 1) // j)
        a, b = x * i, x * j
    print(a + b)


if __name__ == '__main__':
    main()
