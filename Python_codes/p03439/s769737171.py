def get_sex(i):
    print(i, flush=True)
    return input()


def solve(N):
    if N <= 19:
        for i in range(N):
            print(i, flush=True)
            s = input()
            if s == 'Vacant':
                exit()

    low_sex = get_sex(0)
    if low_sex == 'Vacant':
        exit()
    high_sex = get_sex(N - 1)
    if high_sex == 'Vacant':
        exit()

    high, low = N - 1, 0
    while high > low:
        mid = (high + low) // 2
        mid_sex = get_sex(mid)
        if mid_sex == 'Vacant':
            exit()

        if (mid - low) % 2 == 1:
            if mid_sex != low_sex:
                low = mid
                low_sex = mid_sex
            else:
                high = mid
                high_sex = mid_sex
        else:
            if mid_sex != low_sex:
                high = mid
                high_sex = mid_sex
            else:
                low = mid
                low_sex = mid_sex


if __name__ == '__main__':
    solve(int(input()))