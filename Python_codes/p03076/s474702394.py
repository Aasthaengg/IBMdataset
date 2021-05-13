A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

menuTimeList = [A, B, C, D, E]
menuExtraTimeList = [0, 0, 0, 0, 0]

maxExtraTime = 0
for i in range(5):
    extraTime = 0
    if menuTimeList[i] % 10 == 0:
        menuExtraTimeList[i] = 0 
    else:
        extraTime = 10 - menuTimeList[i] % 10
        menuExtraTimeList[i] = extraTime
    if maxExtraTime < extraTime:
        maxExtraTime = extraTime

answer = sum(menuTimeList) + sum(menuExtraTimeList) - maxExtraTime
print(answer)