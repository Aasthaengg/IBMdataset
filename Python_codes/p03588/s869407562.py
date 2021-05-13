def main():
    n = int(input())
    lowest_rank = 0
    lowest_score = 10 ** 9 + 1

    for _ in range(n):
        a, b = map(int, input().split())
        if lowest_rank < a:
            lowest_rank = a
            lowest_score = b

    print(lowest_rank + lowest_score)


if __name__ == "__main__":
    main()
