import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = inintl()

prev = A[0]
ans = 1
sign = 0

for i in range(1,n):
    if A[i] == prev:
        continue
    if A[i] > prev:
        if sign == -1:
            ans += 1
            prev = A[i]
            sign = 0
            continue
        else:
            sign = 1
            prev = A[i]
            continue
    if A[i] < prev:
        if sign == 1:
            ans += 1
            prev = A[i]
            sign = 0
            continue
        else:
            sign = -1
            prev = A[i]
            continue

print(ans)
