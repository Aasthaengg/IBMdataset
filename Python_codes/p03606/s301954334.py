def main():
    groups = int(input())
    answer = 0
    for _ in range(groups):
        reserved = list(map(int, input().split()))
        answer += reserved[1] - reserved[0] + 1
    print(answer)


if __name__ == '__main__':
    main()

