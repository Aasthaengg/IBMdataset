def resolve():
    A = [int(i) for i in input().split()]
    sumA = 0
    for a in A:
        if a == 1:
            sumA += 300000
        elif a == 2:
            sumA += 200000
        elif a == 3:
            sumA += 100000
    if max(A) == 1:
        sumA += 400000
    print(sumA)

resolve()
