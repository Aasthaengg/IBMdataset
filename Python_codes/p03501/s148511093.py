def abc():
    n, a, b = map(int, input().split())
    plan1 = n * a
    plan2 = b
    print(min(plan1, plan2))


abc()
