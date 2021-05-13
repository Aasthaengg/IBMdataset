def resolve():
    N = input()
    minA = 10**5
    for i in range(len(N) - 2):
        minA = min(minA, abs(753 - int(N[i:i + 3])))
    print(minA)


resolve()
