def calc(s):
    n = len(s)
    seq_cnt = []
    cnt, before_c = 0, s[0]
    for c in s:
        if c != before_c:
            seq_cnt.append(cnt)
            cnt = 0
            before_c = c
        cnt += 1
    seq_cnt.append(cnt)
    ret = 0
    for cnt in seq_cnt:
        ret += cnt // 2
    return ret


def main():
    S = input()
    K = int(input())
    N = len(S)
    index = N
    for i, c in enumerate(S):
        if c != S[0]:
            index = i
            break
    if index == N:
        # S consists of single kind of characters
        print(N * K // 2)
    else:
        # S consists of multiple kinds of characters
        print(calc(S[:index]) + (K - 1) * (calc(S[index:] + S[:index])) + calc(S[index:]))


if __name__ == '__main__':
    main()