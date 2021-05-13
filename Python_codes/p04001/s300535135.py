def resolve():
    S = input()
    sumA = 0
    for i in range(2**(len(S) - 1)):
        Stmp = list(S)
        for j in range(len(S) - 2, -1, -1):
            if (i >> j) & 1:
                Stmp.insert(j + 1, "+")
        sumA += eval("".join(Stmp))
    print(sumA)


resolve()
