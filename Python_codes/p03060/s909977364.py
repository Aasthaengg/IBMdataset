# ABC 125: B – Resale
N = int(input())
V = [int(s) for s in input().split()]
C = [int(s) for s in input().split()]

profits = [x - y for x, y in zip(V, C)]
print(sum([k for k in profits if k >= 0]))