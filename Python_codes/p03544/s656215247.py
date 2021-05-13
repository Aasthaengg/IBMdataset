import sys
N = int(input())
if not (1 <= N <= 86):
    sys.exit()

L = [2,1]
if N == 1:
    print(1)
    sys.exit()

for I in range(2,N+2):
    L.append(L[I-1] + L[I-2])
print(L[N])
