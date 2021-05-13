import sys
N = int(input())
K = int(input())

if not ( 1 <= N <= 10 and 1 <= K <= 10 ):
    sys.exit()

start = 1
for I in range(N):
    if start < K:
        start = start * 2
    else:
        start = start + K

print(start)