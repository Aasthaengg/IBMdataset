import sys
input = sys.stdin.readline


n, m = map(int, input().split())

edges = [set() for _ in range(n)]
for _ in range(m):
    _from, to = map(int, input().split())
    edges[_from-1].add(to-1)

first = list(edges[0])

possible = False
while first:
    island = first.pop()
    if n-1 in edges[island]:
        possible = True
        break

if possible:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE ")
