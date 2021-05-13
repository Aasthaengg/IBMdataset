from functools import reduce


def main():
    n, k = tuple(map(int, input().split()))
    s = input().strip()
    start = 0
    count_zero = {}

    for i, c in enumerate(s):
        if c == "0":
            if i == start:
                count_zero[start] = 0

            count_zero[start] += 1
        elif c == "1":
            start = i + 1

    if len(count_zero) <= k:
        print(n)
        return

    count_zero[-1] = 1
    count_zero[n] = 1

    count_zero_list = sorted(count_zero.items(), key=lambda pair: pair[0])

    print(reduce(lambda ans, i:
        max(ans, count_zero_list[i + k + 1][0] - (count_zero_list[i][0] + count_zero_list[i][1])),
        range(0, len(count_zero) - k - 1), 0))


if __name__ == "__main__":
    main()
