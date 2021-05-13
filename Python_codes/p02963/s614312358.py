from math import ceil


def main():
    area = int(input())
    upper_limit = 10 ** 9
    answer = [0, 0, upper_limit, 1, 0, ceil(area / upper_limit)]
    answer[4] = upper_limit * answer[5] - area
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    main()

