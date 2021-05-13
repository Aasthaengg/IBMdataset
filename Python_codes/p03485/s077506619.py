import statistics
import math

a = list(map(int,input().split()))
print( math.ceil(statistics.mean(a)))