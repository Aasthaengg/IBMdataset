def main():
    MOD = 10**9 + 7
    N = int(input())
    T = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    if T[-1] != A[0]:
        return print(0)
    ma_idx_T = T.index(max(T))
    # print(ma_idx_T)
    if A[ma_idx_T] != T[ma_idx_T]:
        return print(0)
    non_fix = [True] * N
    non_fix[0] = False
    non_fix[-1] = False
    for i in range(1, N):
        if T[i-1] < T[i]:
            non_fix[i] = False
            ma_idx_T = i
        else:
            continue

    for i in range(N-1)[::-1]:
        if A[i] > A[i+1]:
            non_fix[i] = False
        else:
            continue
    ans = 1
    # print(non_fix)
    for i, f in enumerate(non_fix):
        if f:
            ans *= min(T[i], A[i])
            ans %= MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()
