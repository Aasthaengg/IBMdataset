def nikkei19q_c():
    N = int(input())
    dish = []
    for i in range(N):
        a, b = map(int, input().split())
        dish.append((a, b))

    prior = sorted(dish, key=lambda x: x[0] + x[1], reverse=True)
    pt_tak, pt_aok = 0, 0

    for i, (a, b) in enumerate(prior):
        if i%2 == 0:
            pt_tak += a
        else:
            pt_aok += b

    ans = pt_tak - pt_aok
    print(ans)

nikkei19q_c()