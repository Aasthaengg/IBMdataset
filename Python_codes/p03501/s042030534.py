import sys
N,A,B = map(int,input().split())

if not (1 <= N <= 20 and 1 <= A <= 100 and 1 <= B <= 2000):
    sys.exit()

if N * A <= B:
    print(N * A)
else:
    print(B)