# ABC 84, C - sunuke festival
import bisect

n = int(input())
A = sorted([int(el) for el in input().split(' ')])
B = [int(el) for el in input().split(' ')]
C = sorted([int(el) for el in input().split(' ')])

total = 0
for b in B:
    total += bisect.bisect_left(A, b) * (len(C) - bisect.bisect_right(C, b))
print(total)
