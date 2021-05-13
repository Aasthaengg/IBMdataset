import sys
from collections import defaultdict
array_8 = defaultdict(int)
N = int(input())
if not ( 1 <= N <= 200 ): sys.exit()

for A in range(2,N+1):
    if A % 2 == 1:
        for I in range(2,N // 2):
            if A % I == 0:
                array_8[A] += 1

result = 0
for J in array_8:
    if array_8[J] == 6:
        result += 1
print(result)