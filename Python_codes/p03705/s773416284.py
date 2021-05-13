# AGC 015: A – A+...+B Problem
N, A, B = [int(s) for s in input().split()]

if A > B or (N == 1 and A != B):
    print(0)
elif A == B or B - A == 1:
    print(1)
else:
    print(B * (N - 2) - A * (N - 2) + 1)