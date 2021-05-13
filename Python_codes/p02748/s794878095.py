import sys
import copy
l = [int(c) for c in input().split()]
A=l[0]
B=l[1]
M=l[2]
a=[int(c) for c in input().split()]
b=[int(c) for c in input().split()]
H = [list(map(int,input().split())) for c in range(M)]

a_sorted = sorted(a)
b_sorted = sorted(b)

MinPrice = a_sorted[0]+b_sorted[0]

for i in range(M):
    if MinPrice > a[H[i][0]-1]+b[H[i][1]-1]-H[i][2]:
        MinPrice = a[H[i][0]-1]+b[H[i][1]-1]-H[i][2]

print(MinPrice)
