# Tenka1 Programmer Beginner Contest 2018: B – Exchange
A, B, K = [int(i) for i in input().split()]

for i in range(1, K + 1):
    if i % 2 == 1:
        A = (A - 1) // 2 if A % 2 == 1 else A // 2
        B += A
    else:
        B = (B - 1) // 2 if B % 2 == 1 else B // 2
        A += B

print(A, B)