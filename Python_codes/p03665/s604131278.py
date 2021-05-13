def comb(n, k):
    if k > n // 2:
        return comb(n, n - k)
    numer = 1
    denom = 1
    for i in range(k):
        numer *= n - i
        denom *= k - i
    return numer // denom


def main():
    N, P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    # 合計を2で割ったあまりが0となるパターンを数える
    cnt_even_bag = len([a for a in A if a % 2 == 0])
    cnt_odd_bag = N - cnt_even_bag
    cnt_even_pattern = 2 ** cnt_even_bag
    cnt_odd_pattern = 0
    for c in range(1, cnt_odd_bag + 1, 2):
        cnt_odd_pattern += comb(cnt_odd_bag, c)
    cnt_even = cnt_even_pattern * cnt_odd_pattern
    if P == 1:
        print(cnt_even)
    else:
        print(2 ** N - cnt_even)


if __name__ == '__main__':
    main()
