import sys
N = int(input())
if not ( 1 <= N <= 100 ):
    sys.exit()

for I in range(N // 4 + 1):
    for J in range(N // 7 + 1):
        if 4 * I + J * 7 == N:
            print('Yes')
            sys.exit()
print('No')