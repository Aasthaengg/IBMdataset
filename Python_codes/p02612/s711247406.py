N = int(input())

A = N % 1000

if A == 0:
    print(0)
else:
    B = 1000 - A
    print(B)
