first = input()
(sA, sB, ) = first.split()
A = int(sA)
B = int(sB)
if B%A == 0:
    print(A+B)
else:
    print(B-A)