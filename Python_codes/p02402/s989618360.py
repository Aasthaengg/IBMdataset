import math

n = input()

a = map(int, raw_input().split())

minNum = 100000000000
maxNum = -100000000000
sumNum = 0

for x in a :
    minNum = min(minNum, x)
    maxNum = max(maxNum, x)
    sumNum += x

minNum, maxNum, sumNum = map(str, [minNum, maxNum, sumNum])

print minNum + ' ' + maxNum + ' ' + sumNum