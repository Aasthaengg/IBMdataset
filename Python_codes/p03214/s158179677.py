import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

m = sum(A) / N

res = 10 ** 9
cost = 10 ** 9
for i, a in enumerate(A):
    if abs(a - m) < cost:
        res = i
        cost = abs(a - m)

print(res)
