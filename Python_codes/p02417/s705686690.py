# Counting Characters
import sys

charList = list('abcdefghijklmnopqrstuvwxyz')
lines = sys.stdin.readlines()
combinedLine = ""
for line in lines:
    line = line.strip("\n").lower()
    combinedLine += line
totalSentence = list(combinedLine)
# print(totalSentence)

for char in charList:
    count = 0
    for i in range(len(totalSentence)):
        if totalSentence[i] == char:
            count += 1
    print(char + ' : ' + str(count))

