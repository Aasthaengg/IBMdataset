def main():
    n = int(input())
    ss = list(input())

    ans = float("inf")
    ans = [0] * n
    cum_sum_w = [0] * (n+1)
    cum_sum_e = [0] * (n+1)
    for i in range(n):
        if ss[i] == 'W':
            add = 1
        else:
            add = 0
        cum_sum_w[i+1] = cum_sum_w[i] + add
    for i in range(n):
        if ss[i] == 'E':
            add = 1
        else:
            add = 0
        cum_sum_e[i+1] = cum_sum_e[i] + add
    for i in range(n):
        ans[i] = cum_sum_w[i] + (cum_sum_e[n] - cum_sum_e[i+1])
    print(min(ans))


if __name__ == "__main__":
    main()
