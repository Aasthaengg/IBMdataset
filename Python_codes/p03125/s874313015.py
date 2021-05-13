a,b = input().split()

A = int(a)
B = int(b)

if B % A == 0:
    print(A + B)
else:
    print(B-A)