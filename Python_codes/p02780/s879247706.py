def main():
    n, k = map(int, input().split())
    P = [int(x) for x in input().split()]
    p_e = list()
    exp = 0
    for p in P:
        # 期待値
        # 累積和
        exp += (1+p)/2
        p_e.append(exp)
    # 初期値
    maxv = p_e[k-1] - 0
    for i in range(1, n-k):
        # 隣接するk個の期待値の和
        p_sum = p_e[k+i] - p_e[i]
        maxv = max(maxv, p_sum)
    print(maxv)
if __name__ == '__main__':
    main()
