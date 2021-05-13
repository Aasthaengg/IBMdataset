# AGC 030: A – Poisonous Cookies
A, B, C = [int(s) for s in input().split()]

if C <= B or C <= A + B:
    print(B + C)
else:
    print(A + B + 1 + B)