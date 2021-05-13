# https://atcoder.jp/contests/abc080/tasks/abc080_c

n = int(input())

shops = []
for _ in range(n):
    s = [int(i) for i in input().split()]
    shops.append(s)

profits = []
for _ in range(n):
    p = [int(i) for i in input().split()]
    profits.append(p)

ans = -1 * float('inf')
for i in range(1, 2 ** 10):
    revenue = 0
    for j in range(n):
        c = 0
        s = shops[j]
        for k in range(10):
            if s[k] and (i >> k) & 1:
                c += 1
        revenue += profits[j][c]
    ans = max(ans, revenue)
print(ans)