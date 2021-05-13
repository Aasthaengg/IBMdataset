def max_f(K, A):
    K += 1
    N = len(A)
    len_K = len('{:b}'.format(K))
    max_KA = max([K, max(A)])
    max_len = len('{:b}'.format(max_KA))
    bin_K = '{{:0{}b}}'.format(max_len).format(K)
    bin_A = ['{{:0{}b}}'.format(max_len).format(a) for a in A]
    bit_A_sum = [sum([int(bin_str[-(i+1)]) for bin_str in bin_A]) for i in range(max_len)]
    bit_K = [int(bin_K[-(i+1)]) for i in range(max_len)]
    f_val = [0 for _ in range(len_K)]
    for free_len in range(len_K):
        if bit_K[free_len] == 0:
            continue
        digit_x = [0 for _ in range(max_len)]
        for j, (ba, bk) in enumerate(zip(bit_A_sum, bit_K)):
            if j < free_len:
                digit_x[j] = max([ba, N - ba])
            elif j == free_len:
                # bit_K[free_len] == 1 -> bit_x[free_len] == 0
                digit_x[j] = ba
            else:
                digit_x[j] = ba if bk == 0 else (N - ba)
        f_val[free_len] = sum([(2**i) * d for i, d in enumerate(digit_x)])
    return int(max(f_val))


def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    print(max_f(K, A))


if __name__ == '__main__':
    main()