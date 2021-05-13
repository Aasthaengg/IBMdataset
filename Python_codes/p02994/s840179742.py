def main():
    N, L = map(int, input().split())

    total = 0
    min_taste = 10 ** 12

    for i in range(1, N + 1):
        taste = L + i - 1
        if abs(taste) < min_taste:
            min_taste = abs(taste)
            min_taste_index = i

    total = N * L + N * (N + 1) // 2 - N
    ans = total - (L + min_taste_index - 1)

    print(ans)


if __name__ == "__main__":
    main()
