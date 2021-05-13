import sys
input = sys.stdin.readline

n = int(input())
A = [int(i) for i in input().strip().split()]
q = int(input())
M = [int(i) for i in input().strip().split()]

comb = set()

for i in range(2 ** n):
    _tmp = 0
    for j in range(n):
        if (i >> j) & 1:
            _tmp += A[j]
    comb.add(_tmp)

for m in M:
    if m in comb:
        print("yes")
    else:
        print("no")

