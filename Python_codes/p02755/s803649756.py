import math

A, B = map(int, input().split())

A_min = math.ceil(12.5*A)
A_max = math.ceil(12.5*(A+1)) - 1

B_min = math.ceil(10*B)
B_max = math.ceil(10*(B+1)) - 1

for i in range(B_min, B_max+1):
    if A_min <= i <= A_max:
        print(i)
        break
    if i == B_max:
        print(-1) 