def main():
    n, m, k = map(int, input().split())
    answer = False
    for i in range(n + 1):
        if answer:
            break
        for j in range(m + 1):
            if i * j + (n - i) * (m - j) == k:
                answer = True
                break
    print("Yes" if answer else "No")


if __name__ == '__main__':
    main()

