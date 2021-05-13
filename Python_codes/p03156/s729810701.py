def main():
    questions = int(input())
    a, b = map(int, input().split())
    score = list(map(int, input().split()))
    count_range = [0, 0, 0]
    for s in score:
        if s <= a:
            count_range[0] += 1
        elif s <= b:
            count_range[1] += 1
        else:
            count_range[2] += 1
    print(min(count_range))


if __name__ == '__main__':
    main()

