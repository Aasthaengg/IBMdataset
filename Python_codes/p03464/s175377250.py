import sys
K = int(input())
A = list(map(int, input().split()))
minA = 2
maxA = 2
for ai in A[::-1]:
    if minA <= ai <= maxA:
        minA = ai
        maxA = maxA - maxA%ai + ai - 1
    elif ai < minA:
        minA = minA + ai * int(minA%ai>0) - minA%ai
        maxA = maxA - maxA%ai + ai - 1
    elif ai > maxA:
        print(-1)
        sys.exit()
if minA > maxA:
    print(-1)
else:
    print(minA, maxA)