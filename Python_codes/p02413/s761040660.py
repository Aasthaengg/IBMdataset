# coding: utf-8
height, width = list(map(int, input().split(" ")))
answer = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

for row in range(height):
    column = 0
    sumOfColumn = 0
    for value in list(map(int, input().split(" "))):
        answer[row][column] = value
        sumOfColumn += value
        column += 1
    answer[row][column] = sumOfColumn
    
for columnIndex in range(width + 1):
    sumOfRow = 0
    for rowIndex in range(height):
        value = answer[rowIndex][columnIndex]
        sumOfRow += value
    answer[height][columnIndex] = sumOfRow

for row in answer:
    print(" ".join(map(str, row)))