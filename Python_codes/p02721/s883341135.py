def main():
    from bisect import bisect_left, bisect_right

    N, K, C = map(int, input().split())
    s = input()

    L = [0] * (N + 2)
    R = [0] * (N + 2)
    # 1-indexedで管理した
    # 貪欲に端から配置した場合に達成可能な
    # 累積配置数

    need = [0] * N

    i = 0
    while i < N:
        if s[i] == 'o':
            L[i + 1] = 1
            need[i] += 1
            i += C + 1
        else:
            i += 1

    i = N - 1
    while i >= 0:
        if s[i] == 'o':
            R[i + 1] = 1
            need[i] += 1
            i -= C + 1
        else:
            i -= 1

    for i in range(N):
        L[i + 1] += L[i]
        R[i + 1] += R[i]

    ans = []
    for i in range(N):
        if need[i] == 2:
            li = bisect_left(L, L[i])  # 1-indexed
            if R[i + 1] == R[i + 2]:
                ri = bisect_right(R, R[i + 2]) + 1
            else:
                ri = i + 2  # 1-indexed
            d = (ri - li + 1 <= C)
            except_i = L[i] + (R[N] - R[i + 1]) - d
            if except_i < K:
                ans.append(i + 1)

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

# 前後両端について
# それぞれから貪欲に配置した累積配置数を準備
# 必ず働く日は
# 前から貪欲に配置したケースと
# 後ろから貪欲に配置したケースの重なりに含まれる必要があり、
# そのような重なり(need==2)について
# その日に働かないとした場合の前後の累積配置数の和がK未満なら働く必要がある
