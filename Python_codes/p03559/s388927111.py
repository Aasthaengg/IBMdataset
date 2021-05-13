import sys
import os
import re
import datetime
import bisect

####### main #######

N = int(input())

partsNumA = sorted(map(int, input().split()))
partsNumB = sorted(map(int, input().split()))
partsNumC = sorted(map(int, input().split()))

# Bに対してAの個数のBによるループ
partsNumSumBa = []
sumA = 0
for curPartsB in partsNumB:
    indexA = bisect.bisect_left(partsNumA, curPartsB)
    numA = indexA
    sumA += numA
    partsNumSumBa.append(sumA)

# Cに対してBの個数のCによるループ
sumBAll = 0
for curPartsC in partsNumC:
    indexB = bisect.bisect_left(partsNumB, curPartsC)
    if indexB == 0:
        continue
    numB = partsNumSumBa[indexB - 1]
    sumBAll += numB

print(sumBAll)