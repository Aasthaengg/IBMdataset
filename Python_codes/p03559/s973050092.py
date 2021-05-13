def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_right
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    b_comb_accum = [0] * (N+1)
    for i in range(N-1, -1, -1):
        c_min_ind = bisect_right(C, B[i])
        b_comb_accum[i] = b_comb_accum[i+1] + N - c_min_ind
    ans = 0
    for a in A:
        b_min_ind = bisect_right(B, a)
        ans += b_comb_accum[b_min_ind]
    print(ans)


if __name__ == '__main__':
    main()