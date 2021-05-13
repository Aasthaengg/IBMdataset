def resolve():
    a, b, m = map(int, input().split())
    a_s = [int(i) for i in input().split()]
    b_s = [int(i) for i in input().split()]

    min_cost = min(a_s) + min(b_s)
    for _ in range(m):
        a_i, b_i, c_i = map(int, input().split())
        cost = a_s[a_i-1] + b_s[b_i-1] - c_i
        if cost < min_cost:
            min_cost = cost

    print(min_cost)


resolve()