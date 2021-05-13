A, B, C = [int(x) for x in input().split()]
Z = 0
if C > A:
    Z = A
    C -= A
else:
    Z = C
    C = 0
if C > B:
    Z += (B * 2)
    C -= B
else:
    Z += (B + C)
    C = 0
if C > 0:
    Z += 1
print(Z)