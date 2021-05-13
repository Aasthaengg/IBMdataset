import sys
import math

X = int(sys.stdin.readline().strip())

# i秒までに進める最大の距離
max_t = int(math.sqrt(2*X)) + 1
# print(max_t)
for i in range(max_t + 1):
    if i * (i+1) >= 2 * X:
        break

print(i)