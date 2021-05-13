import sys

N, A, B = map(int, input().split())

if A > B:
    print(0)
    sys.exit()
elif N == 1:
    if A != B:
        print(0)
    else:
        print(1)
else:
    print((N - 2) * (B - A) + 1)
