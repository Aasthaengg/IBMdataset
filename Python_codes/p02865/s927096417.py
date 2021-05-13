num = int(input())
numList = list(range(0, num))
listLength = len(numList)
counter = 0

#print(numList)

m = [0] * 10000000

for i in range(0, listLength):
    m[numList[i]]
    m[numList[i]] += 1

secondCount = 0

for i in range(0, listLength):
    secondCount += m[num - numList[i]]
    if (num - numList[i] == numList[i]):
        secondCount -= 1

print(int(secondCount / 2))