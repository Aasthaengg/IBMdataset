import math
while True:
    n = float(input())
    if n == 0:
        break
    s = map(int, raw_input().split())
    mean = sum(s) / n
    std = math.sqrt(sum([(si - mean)**2 for si in s]) / n)
    print std