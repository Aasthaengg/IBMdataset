def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # min_l[i]: i番目以前の最小値
    min_l = [a[0]]
    for i in range(1, n):
        if min_l[-1] < a[i]:
            min_l.append(min_l[-1])
        elif min_l[-1] == a[i]:
            min_l.append(min_l[-1])
        else:
            min_l.append(a[i])

    # max_l[i]: i番目以降の最大値
    max_l = [0] * n
    max_l[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        if max_l[i+1] < a[i]:
            max_l[i] = a[i]
        else:
            max_l[i] = max_l[i+1]

    profit = []
    for i in range(n-1):
        profit.append(max_l[i+1] - min_l[i])

    max_profit = profit[0]
    for i in range(1, n-1):
        if max_profit < profit[i]:
            max_profit = profit[i]
    
    ans = 0
    for i in range(n-1):
        if max_l[i+1] - a[i] == max_profit:
            ans += 1
    print(ans)

main()