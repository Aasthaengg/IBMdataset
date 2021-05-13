def actual(n, V, C):
    # 購入するとプラスになるものだけ買って合計でおk
    sale_jewels = []

    for v, c in zip(V, C):
        if v - c > 0:
            sale_jewels.append(v - c)

    return sum(sale_jewels)

    # return sum([v - c for v, c in zip(V, C) if v - c > 0])


n = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

print(actual(n, V, C))