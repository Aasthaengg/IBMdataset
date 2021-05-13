def resolve():
    allPt = []
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                allPt.append(int(str(i) + str(j) + str(k) + str(j) + str(i)))
    A, B = [int(i) for i in input().split()]
    cnt = 0
    for i in allPt:
        if A <= i and i <= B:
            cnt += 1
    print(cnt)


resolve()
