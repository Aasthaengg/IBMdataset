TestNum = int(input())
TimeList = list(map(int,input().split()))
DrinkNum = int(input())
DrinkList = [list(map(int, input().split())) for _ in range(DrinkNum)]
TimeSum = sum(TimeList)
for i in DrinkList:
    print(TimeSum - (TimeList[i[0] -1] - i[1]))