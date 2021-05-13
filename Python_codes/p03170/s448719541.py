def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))

    dp = [0] * (k+1)
    # dp[0] == 0 ならばそのとき手番の者（先手）の負け
    for i in range(k+1):
        for a in a_list:
            if dp[i] == 0:
                idx = i + a
                if idx < k+1:
                    dp[idx] = 1

    if dp[k] == 0:
        print('Second')
    else:
        print('First')


if __name__ == '__main__':
    main()
