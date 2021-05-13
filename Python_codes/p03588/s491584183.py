def main():
    n = int(input())
    max_score = 0
    max_index = 0
    min_score = float("inf")
    min_index = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if max_index > a:
            max_index = a
            max_score = b
        if min_index < a:
            min_index = a
            min_score = b
    print(min_index + min_score)


if __name__ == '__main__':
    main()

