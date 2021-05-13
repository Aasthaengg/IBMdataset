import statistics as stat
import math
N = int(input())
A = list(map(int, input().split()))
linear = [i+1 for i in range(N)]
B = [x-y for (x, y) in zip(A, linear)]
med = stat.median(B)
med_up = math.ceil(med)
med_low = math.floor(med)
count_up = 0
count_low = 0
for i in range(N):
    count_up += abs(B[i] - med_up)
    count_low += abs(B[i] - med_low)
print(min(count_up, count_low))