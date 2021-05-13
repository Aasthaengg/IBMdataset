import sys

read = sys.stdin.read

N, A, B, *P = map(int, read().split())

a = 0
b = 0
c = 0
for i in P:
    if i <= A:
        a += 1
    elif A < i <= B:
        b += 1
    else:
        c += 1

print(min(a, b, c))
