#解説確認後

import math
N = int(input())
Carry = []
for i in range(5):
    Carry.append(int(input()))
min_num = min(Carry)

print(math.ceil(N/min_num)+4)
