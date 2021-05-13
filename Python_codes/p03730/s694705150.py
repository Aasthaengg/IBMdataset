import sys
A, B, C = map(int, input().split())
N = A
while N < A * B:
    if N % B == C:
        print('YES')
        sys.exit()
    N += A
print('NO')