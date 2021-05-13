import statistics
import math

n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    A[i] = A[i]-i-1
A.sort()
m = statistics.median(A)

f = math.floor(m)
c = math.ceil(m)
sum_f = 0
sum_c = 0

for i in range(n):
    sum_f += abs(A[i]-f)
    sum_c += abs(A[i]-c)
    
print(min(sum_f, sum_c))