import math
loan = 100000
for i in range(int(input())):
    loan += math.ceil(loan * 0.05 / 1000) * 1000
print(loan)