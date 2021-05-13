#!/usr/bin/env python

#get dimensions
n, m = input().split()
n = int(n)
m = int(m)

nmmatrix = []
mvector = []
result = []

#make matrix
for x in range(n):
    row = input()
    rowSplit = row.split()
    for y in range(len(rowSplit)):
        rowSplit[y] = int(rowSplit[y])
    nmmatrix.append(rowSplit)

#makevector
for x in range(m):
    mvector.append(int(input()))

#multiplication
for x in range(n):
    value = 0
    for y in range(m):
        value += nmmatrix[x][y]*mvector[y]
    result.append(value)
    
#print result
for x in result:
    print(x)