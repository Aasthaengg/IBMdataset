import sys

N = int(input())

for i in range(1, 10):
    if N % i == 0:
        if 1 <= N/i <= 9:
            print('Yes')
            sys.exit(0)
        else:
            continue

print('No')