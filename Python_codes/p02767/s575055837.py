def stamina(x, p):
    return (x - p) ** 2


def resolve():
    N = int(input())
    Xs = list(map(int, input().split()))

    min_sum = 10 ** 10
    for p in range(1, 101):
        s_sum = 0
        for p_x in Xs:
            s_sum += stamina(p_x, p)

        min_sum = min(min_sum, s_sum)

    print(min_sum)
resolve()