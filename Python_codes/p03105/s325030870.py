A, B, C = input().strip().split()
A, B, C = [int(A), int(B), int(C)]

if B/A < 1:
    print(0)
elif B/A > C:
    print(C)
else:
    print(int(B/A))