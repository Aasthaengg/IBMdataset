# -*- coding: utf-8 -*-

# リュカ数

#L0 = 2
#L1 = 1
#L2 = 1 + 2 = 3
#L3 = 3 + 1 = 4
#L4 = 4 + 3 = 7
#L5 = 7 + 4 = 11
#L6 = 11 + 7 = 18

N = int(input())

Li_2 = 2
Li_1 = 1
Li = 1

for i in range(2, N + 1):
    Li = Li_1 + Li_2
    Li_2, Li_1 = Li_1, Li

print(Li)