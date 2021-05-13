line = input()
A, B = [int(n) for n in line.split()]
r1 = A+B
r2 = A-B
r3 = A*B

r4 = max(r1, r2)
r4 = max(r4, r3)
print(r4)