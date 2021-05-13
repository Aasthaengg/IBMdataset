def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    rate_list = [0] * 9

    for a in a_list:
        rate = a // 400
        if rate < 8:
            rate_list[rate] += 1
        else:
            rate_list[-1] += 1

    min_cnt = 0
    for i in range(8):
        if rate_list[i] > 0:
            min_cnt += 1

    print(max(min_cnt, 1), min_cnt + rate_list[-1])


if __name__ == "__main__":
    main()
