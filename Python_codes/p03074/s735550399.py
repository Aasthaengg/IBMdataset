def main():
    N, K = list(map(int, input().split(' ')))
    S = input()
    # Find 0->1 / 1->0 patterns
    zero_one_indices = [0]
    one_zero_indices = [0] if S[0] == '0' else []
    before_c = None
    for i, c in enumerate(S):
        if (before_c, c) == ('0', '1'):
            zero_one_indices.append(i)
        elif (before_c, c) == ('1', '0'):
            one_zero_indices.append(i)
        before_c = c
    max_length = 0
    for k in range(len(zero_one_indices)):
        if k + K < len(one_zero_indices):
            # 1_seq + [0_seq, 1_seq] * K
            length = one_zero_indices[k + K] - zero_one_indices[k]
        else:
            length = N - zero_one_indices[k]
        max_length = max([length, max_length])
    print(max_length)


if __name__ == '__main__':
    main()
