import math
A = [int(input()) for _ in range(5)]
B = 0
C = 0
for i in range(5):
    B += math.ceil(A[i]/10)*10
    C = max(math.ceil(A[i]/10)*10 - A[i],C)
print(B-C)
