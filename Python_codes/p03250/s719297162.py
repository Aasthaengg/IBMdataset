def resolve():
    import itertools
    A = [i for i in input().split()] + ["+"]
    maxA = 0
    for a in itertools.permutations(A):
        if a[0] != "+" and a[-1] != "+":
            maxA = max(maxA, eval("".join(a)))
    print(maxA)


resolve()
