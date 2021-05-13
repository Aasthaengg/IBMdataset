def calc_n_range(a):
    min_n = max_n = 2

    for curr_a in reversed(a):
        min_n = ((min_n + curr_a - 1) // curr_a) * curr_a
        if min_n > max_n:
            return None
        max_n = max_n - max_n % curr_a + curr_a - 1

    return min_n, max_n


def main():
    input()
    a = list(map(int, input().split()))

    n_range = calc_n_range(a)
    if n_range:
        print(*n_range)
    else:
        print(-1)


if __name__ == '__main__':
    main()
