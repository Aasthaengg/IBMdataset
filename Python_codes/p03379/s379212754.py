import math
n = int(input())

lis = list(map(int, input().split()))

nlis = sorted(lis)

med1 = nlis[n//2-1]
med2 = nlis[n//2]

for i in lis:
    if i <= med1:
        print(med2)
    else:
        print(med1)