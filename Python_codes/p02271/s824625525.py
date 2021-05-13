from itertools import combinations
n = int(input())
A = tuple(map(int, input().split()))
B = set(A)
for i in range(2, n + 1):
    for C in combinations(A, i):
        B.add(sum(C))
q = int(input())
for m in map(int, input().split()):
    print("yes" if m in B else "no")

