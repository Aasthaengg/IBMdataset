import math
A = [int(input()) for _ in range(5)]
ad = 0
rm = 0
for i in range(5):
    ad += math.ceil(A[i]/10)*10
    rm = max(math.ceil(A[i]/10)*10 - A[i],rm)
print(ad-rm)