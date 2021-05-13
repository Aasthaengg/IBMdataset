import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))
A.sort()

s = 0
res = 0

for i in range(N - 1):
    s += A[i]
    if s * 2 >= A[i + 1]:
        res += 1
    else:
        res = 0

print(res + 1)
