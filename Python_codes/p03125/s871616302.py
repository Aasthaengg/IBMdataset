A, B = [int(s) for s in input().split(' ')]
print(A + B if B % A == 0 else B - A)