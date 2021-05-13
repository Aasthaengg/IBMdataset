import sys
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if not (1 <= A and B and C and D <= 1000):
    sys.exit()

result = 0
if A >= B:
    result += B
else:
    result += A
if C >= D:
    result += D
else:
    result += C
print(result)