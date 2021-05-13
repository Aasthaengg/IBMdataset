import itertools
n, m, x = map(int, input().split())
ca = []
for _ in range(n):
    ca.append(list(map(int, input().split())))

prices = []
best_skill = [0]*m
for i in range(1, n+1):
    n_list = [i for i in range(n)]
    for N in itertools.combinations(n_list, i):
        skill = [0]*m
        price = 0
        for j in N:
            price += ca[j][0]
            for k in range(1, m+1):
                skill[k-1] += ca[j][k]
        if min(skill) >= x:
            prices.append(price)

if prices:
    print(min(prices))
else:
    print(-1)