import sys

n = int(input())
A = [int(a) for a in input().split()]

q = int(input())
M = [int(m) for m in input().split()]

makable = set()

for i in range(2 ** n):
    total = 0

    for j in range(n):
        b = i % 2
        total += A[j] * b
        i //= 2

    makable.add(total)

# print(makable)

for m in M:
    if m in makable:
        print("yes")
    else:
        print("no")