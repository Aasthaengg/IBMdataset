from statistics import median

A, B, C = [int(x) for x in input().split()]

low = min(A, B, C)
mid = median([A, B, C])
huge = max(A, B, C)

if huge % 2 == 0:
    print(0)
else:
    red = low*mid*(huge//2)
    blue = low*mid*(huge//2+1)

    print(blue-red)
