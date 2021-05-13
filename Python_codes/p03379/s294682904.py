import math
import statistics
n = int(input())
x = [int(i) for i in input().split()]

x_sorted = sorted(x)
lower_med = statistics.median(x_sorted[1:])
upper_med = statistics.median(x_sorted[:len(x)-1])

median = statistics.median(x)

for i in range(n):
    if x[i] < median:
        print(lower_med)
    else:
        print(upper_med)
