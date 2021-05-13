def main():
    info_num = int(input())
    min_score_index = 0
    min_score = float("inf")
    for _ in range(info_num):
        a, b = map(int, input().split())
        if min_score_index < a:
            min_score_index = a
            min_score = b
    print(min_score + min_score_index)


if __name__ == '__main__':
    main()

