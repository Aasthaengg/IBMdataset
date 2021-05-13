# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
AB = [lr() for _ in range(M)]
V = [x for x in range(N+1)]
total = N * (N-1) // 2

def find(A, x):
    parent = A[x]
    if parent == x: return x
    root = find(A, parent)
    A[x] = root
    return root

def union(A, x, y):
    root, second = find(A, x), find(A, y)
    if root > second:
        second, root = root, second
    A[second] = root

conv = 0
answer = []
group = [1] * (N+1)
for a, b in AB[::-1]:
    answer.append(total - conv)
    root_A = find(V, a); root_B = find(V, b)
    if root_A != root_B:
        conv += group[root_A] * group[root_B]
        group[root_A] += group[root_B]
        group[root_B] = group[root_A]
        union(V, a, b)

for x in answer[::-1]:
    print(x)
