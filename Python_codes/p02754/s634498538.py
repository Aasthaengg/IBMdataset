import sys
N, A, B = map(int, input().split())

if A == 0:
    print(0)
    sys.exit()

print(A * (N // (A + B)) + min(A, N % (A + B)))