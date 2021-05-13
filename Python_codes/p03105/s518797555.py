line = input()
A, B, C = [int(n) for n in line.split()]
D = int(B/A)
if D >= C:
    print(C)
else:
    print(D)