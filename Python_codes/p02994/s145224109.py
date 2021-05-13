import math

N, L = map(int, input().split())

sum = 0
minimum = 99999
for i in range(1,N+1):
    aji = L + i - 1
    sum += aji
    if (math.fabs(minimum) > math.fabs(aji)):
        minimum = aji

print(sum - minimum)