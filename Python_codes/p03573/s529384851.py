A = [int(x) for x in input().split()]
B = sorted(A)
if B[0] == B[1]:
    print(B[2])
else:
    print(B[0])