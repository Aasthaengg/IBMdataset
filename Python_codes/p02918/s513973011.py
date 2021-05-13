def main():
    N, K = list(map(int, input().split(' ')))
    S = input()
    char_change_cnt = 0
    before_char = S[0]
    for c in S:
        if before_char == c:
            continue
        before_char = c
        char_change_cnt += 1
    char_change_cnt -= min([char_change_cnt, 2 * K])
    print(N - char_change_cnt - 1)


if __name__ == '__main__':
    main()