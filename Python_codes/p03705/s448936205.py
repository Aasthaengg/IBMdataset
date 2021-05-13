import sys
N, A, B = map(int, input().split())

if A > B:
    print(0)
    sys.exit(0)
if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
    sys.exit(0)

x = B*(N-1)+A
n = A*(N-1)+B
print(x-n+1)