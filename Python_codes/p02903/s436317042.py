import math

## only rebel input techniques allowed.
input = str(input()).split(" ")
for index in range(len(input)):
    input[index] = int(input[index])
h, w, a, b = input[0], input[1], input[2], input[3]

## make an array of zeros
array = []
for index1 in range(h):
    row = []
    for index2 in range(w):
        row.append(0)
    array.append(row)

## okay so now we have an array of zeros
## and all we have to do is look at each row and column
def populate( h, w, a, b, array):
    rowCounter = []
    columnCounter = []
    for index in range(h):
        rowCounter.append(0)
    for index in range(w):
        columnCounter.append(0)

    for rowIndex in range(h):
        for colIndex in range(w):
            ## if after we add a one nothing is violated
            if ((rowCounter[rowIndex] < a or w  - rowCounter[rowIndex] > a) and (columnCounter[colIndex] < b or h - columnCounter[colIndex] > b)):
                array[rowIndex][colIndex] = 1
                rowCounter[rowIndex] += 1
                columnCounter[colIndex] += 1

    for element in rowCounter:
        if (min(element, w - element) != a):
            return -1
    for element in columnCounter:
        if (min(element, h - element) != b):
        ##if (element != b and h - elemet != b):
            return -1
    return array

def display(array):
    if (array == -1):
        print("-1")
        pass
    else:
        strings = []
        for row in array:
            string = ""
            for index in range(len(row)):
                if (index != len(row) - 1):
                    string += str(row[index])
                else:
                    string += str(row[index])
            strings.append(string)
        for element in strings:
            print(element)
##print("here")
"""
for h in range(1, 30):
    for w in range(1,30):
        for a in range(0, math.floor(w/2) + 1):
            for b in range(0, math.floor(h/2)+1):
                array = []
                for index1 in range(h):
                    row = []
                    for index2 in range(w):
                        row.append(0)
                    array.append(row)
                if (populate(h, w, a, b, array) == -1):
                    print(h,w,a,b)
"""
##print("done")
display(populate(h, w, a, b, array))
## we could also do this problem by splitting the array into two or four chuncks of ones and zeros
## but I cannot be bothered.
