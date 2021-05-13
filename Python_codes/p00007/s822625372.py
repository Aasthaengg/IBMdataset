import math
loan = 100000
n = int(input())
for i in range(n):
    loan += math.ceil(loan * 0.05 / 1000) * 1000
print(loan)