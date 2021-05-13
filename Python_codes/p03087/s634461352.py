def main():
    n, q = map(int, input().split())
    ss = list(input())
    lrs = [list(map(int, input().split())) for _ in range(q)]
    cum_sum = [0] * n
    for i in range(1, n):
        if ss[i-1] == 'A' and ss[i] == 'C':
            cum_sum[i] += 1
        cum_sum[i] += cum_sum[i-1]
    for l, r in lrs:
        print(cum_sum[r-1]-cum_sum[l-1])


if __name__ == "__main__":
    main()
