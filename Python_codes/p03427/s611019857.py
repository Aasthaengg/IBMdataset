def resolve():
    N = int(input())
    NList = list(str(N))
    maxA = eval("+".join(NList))
    maxA = max(maxA, eval(
        "+".join(list(str(int(NList[0]) - 1) + "9" * (len(NList) - 1)))))
    print(maxA)


resolve()
