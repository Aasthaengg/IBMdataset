import sys
N = int(input())
A = int(input())

if N < 1 or N > 100:
    sys.exit()
if A < 0 or A > N ** 2:
    sys.exit()

print(N ** 2 - A)