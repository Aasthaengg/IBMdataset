def main():
    limit, remainder_min = map(int, input().split(" "))
    answer = 0
    if remainder_min:
        for i in range(1, limit + 1):
            answer += max(0, i - remainder_min) * (limit // i) + max(0, limit % i - remainder_min + 1)
    else:
        answer = limit ** 2
    print(answer)


if __name__ == '__main__':
    main()