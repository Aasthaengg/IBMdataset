import statistics
import math

x = map(int, input().split())

print(math.ceil(statistics.mean(x)))