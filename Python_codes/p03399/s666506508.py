A = int(input())
B = int(input())
C = int(input())
D = int(input())

cst = 0
if A >= B:
    cst += B
else:
    cst += A

if C >= D:
    cst += D
else:
    cst += C
print(cst)