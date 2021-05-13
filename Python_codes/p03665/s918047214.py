import sys

N, P = map(int, input().split())
A = list(map(int, sys.stdin.readline().rsplit()))

even = odd = 0
for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

if odd == 0 and P == 0:
    print(2 ** even)
elif odd == 0 and P == 1:
    print(0)
else:
    print(2 ** (N - 1))
