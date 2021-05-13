import sys
import math

monney = 100000
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    monney = math.ceil(monney * 1.05 / 1000) * 1000
print(monney)