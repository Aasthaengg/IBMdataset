def calc_minkowski_distance(x1, x2, p):
    """calc L_p norm(finite dimension)

    Args:
        x1: vector1
        x2: vector2
        p: p in L_p

    Returns:
        L_p distance between x1 and x2 (float)
    """
    if p == "inf":
        return max([abs(x[0] - x[1]) for x in zip(x1, x2)])
    else:
        return sum([abs(x[0] - x[1]) ** (float(p)) for x in zip(x1, x2)]) ** float(1.0 / p)


target = [1, 2, 3, "inf"]
dimension = int(raw_input())
x1 = [float(x) for x in raw_input().split()]
x2 = [float(x) for x in raw_input().split()]
for p in target:
    print(calc_minkowski_distance(x1, x2, p))