def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    ri = 0
    cur_sum = 0
    for le in range(N):
        while ri < N and cur_sum + A[ri] == cur_sum ^ A[ri]:
            cur_sum += A[ri]
            ri += 1
        ans += ri - le
        if le == ri:
            ri += 1
        else:
            cur_sum -= A[le]
    print(ans)


if __name__ == '__main__':
    main()
