N = [int(i) for i in input().split()]

answerList = []

for i in range(N[0]):
    answerList.append(0)

for i in range(N[0]):
    if i > 0:
        for j in range(N[0]):
            if j + 1 > i > 0:
                calculateList = [abs(j + 1 - i),
                                 abs(N[1] - i) + 1 + abs(j + 1 - N[2]),
                                 abs(N[2] - i) + 1 + abs(j + 1 - N[1])]
                answer = min(calculateList)
                answerList[answer] = answerList[answer] + 1

for i in range(N[0] - 1):
    print(answerList[i + 1])