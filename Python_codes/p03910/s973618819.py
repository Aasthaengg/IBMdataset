def main():
    n = int(input())
    k = int((2 * n) ** 0.5) - 1
    while k * (k + 1) // 2 < n:
        k += 1
    s = k * (k + 1) // 2 - n
    [print(i) for i in range(1, k + 1) if i != s]

if __name__ == '__main__':
    main()
