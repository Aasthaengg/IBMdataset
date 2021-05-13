# -*- coding:utf-8 -*-
n = int(input())

PosList = []
TempSum = 0
ReturnSum = 0

PosList = list(map(int,input().split()))


for pos in range(1,101):
    TempSum = 0
    for nPos in range(n):
        TempSum += (pos - PosList[nPos])**2
    if pos == 1:
        ReturnSum = TempSum
    elif ReturnSum > TempSum:
        ReturnSum = TempSum
    """
    print("Position = "+str(pos))
    print("TempSum = "+ str(TempSum))
    print("ReturnSum = " + str(ReturnSum))
    print("----------------------------")
    """

print(ReturnSum)