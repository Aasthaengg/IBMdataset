from sys import stdin
import sys

n,m,k = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]

cc = []
count = 0
sumA = 0

for i in range(n):
    sumA_ = sumA + A[i]
    if sumA_ > k: break

    sumA = sumA_
    count = count + 1

maxA = count

sumB = 0
j = 0

for i in range(maxA+1):
    if i != 0:
        count = count - 1
        sumA = sumA - A[maxA-i]

    while True:
        sumB_ = sumB + B[j]

        if sumA + sumB_ > k:
            cc.append(count)
            break

        sumB = sumB_
        count = count + 1
        j = j + 1

        if j == m:
            cc.append(count)
            break

    if j == m:
        break


if cc == []:
    print (0)
else:
    print (max(cc))




