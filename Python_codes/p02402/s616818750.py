num = int(input())
inData = [0] * num
inData = [int(i) for i in input().split()]
minVal = min(inData)
maxVal = max(inData)
sumVal = sum(inData)

print(minVal, maxVal, sumVal)
