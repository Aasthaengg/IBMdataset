from sys import stdin
import sys
import math

[A, B, C, D, E, F] = list(map(int, stdin.readline().rstrip().split()))

## F
# F >= 100 * A * a + 100 * B * b + C * c + D * d

## E
# C * c + D * d <= (100 * A * a + 100 * B * b) * E / 100
# 100 * (C * c + D * d) <= (100 * A * a + 100 * B * b) * E
# 100 * (C * c + D * d) / (100 * A * a + 100 * B * b) <= E


maximum_ratio = 0
max_a = 0
max_b = 0
max_c = 0
max_d = 0

for a in range(F // (100 * A) + 1):
    for b in range(F // (100 * B) + 1):
        for c in range(F // 2 // C + 1):
            for d in range(F // 2 // D + 1):
                if 100 * A * a + 100 * B * b + C * c + D * d <= F:
                    if 0 == (100 * A * a + 100 * B * b):
                        continue

                    sugar_ratio = 100 * (C * c + D * d) / (100 * A * a + 100 * B * b)
                    if E >= sugar_ratio and maximum_ratio <= sugar_ratio:
                        maximum_ratio = sugar_ratio
                        max_a = a
                        max_b = b
                        max_c = c
                        max_d = d
                else:
                    break

print("%d %d" % (100 * A * max_a + 100 * B * max_b + C * max_c + D * max_d, C * max_c + D * max_d))
