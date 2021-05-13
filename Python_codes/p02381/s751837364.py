# Standard Deviation

end = 0
while end == 0:
    studentAmount = int(input())
    if studentAmount == 0:
        end += 1
    else:
        scoreData = [int(i) for i in input().rstrip().split()]
        totalScore = 0
        for score in scoreData:
            totalScore += score
        averageScore = totalScore / studentAmount
        # print('Average: ' + str(averageScore))
        totalSquareDistance = 0
        for score in scoreData:
            totalSquareDistance += (score - averageScore) ** 2
        variance = totalSquareDistance / studentAmount
        # print('Variance: ' + str(variance))
        standardDeviation = variance ** 0.5
        # print('Standard Deviation: ', end = '')
        print(str(standardDeviation))

