def main():
    n = int(input())
    rate_count = [0] * 13
    a = tuple(map(int, input().split()))
    for ae in a:
        rank = ae // 400
        rate_count[rank] += 1

    reds = sum(rate_count[8:])
    res = 0
    for i1 in range(8):
        res += rate_count[i1] > 0
    r_min = max(res, 1)
    r_max = res + reds
    print(r_min, r_max)

if __name__ == '__main__':
    main()