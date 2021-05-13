import sys
import os
import re
import datetime
import bisect

def Test(value):
    a = [1,3,5]
    #x = 4

    insert_index = bisect.bisect_left(a, value)
    
    print("insert_index = ", insert_index)
    
if False:   
    while(True): 
        Test(int(input('? ')));
    sys.exit()
 
N = int(input())

partsNumA = sorted(map(int, input().split()))
partsNumB = sorted(map(int, input().split()))
partsNumC = sorted(map(int, input().split()))

# Bに対してAの個数のBによるループ
partsNumSumBa = []
sumA = 0
#for i in range(N):
for curPartsB in partsNumB:
    indexA = bisect.bisect_left(partsNumA, curPartsB)
    numA = indexA
    sumA += numA
    partsNumSumBa.append(sumA)

if False:
    print("Sorted A" , partsNumA)
    print("Sorted B" , partsNumB)
    print("Sorted C" , partsNumC)

    print("B loop" , partsNumSumBa)

# Cに対してBの個数のCによるループ
sumBAll = 0
for curPartsC in partsNumC:
    indexB = bisect.bisect_left(partsNumB, curPartsC)
    if indexB == 0:
        continue
    numB = partsNumSumBa[indexB - 1]
    sumBAll += numB
        
print(sumBAll)