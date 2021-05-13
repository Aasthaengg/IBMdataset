def main():
    n, k = map(int, input().split())
    h_list = [int(input()) for _ in range(n)]
    h_list.sort(reverse=True)

    min_diff = 10 ** 9

    for i in range(n - k + 1):
        diff = h_list[i] - h_list[i + k - 1]
        if diff < min_diff:
            min_diff = diff

    print(min_diff)


if __name__ == "__main__":
    main()
