import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    inf=10**10
    to = defaultdict(list)
    n, m = map(int, input().split())
    for _ in range(m):
        l, r, d = map(int, input().split())
        l, r = l - 1, r - 1
        to[l].append([r, d])
        to[r].append([l, -d])
    pos = [inf] * n
    for root in range(n):
        if pos[root] != inf: continue
        pos[root] = 0
        stack = [[root, 0]]
        while stack:
            u, p = stack.pop()
            for v, d in to[u]:
                if pos[v] == inf:
                    stack.append([v, p + d])
                    pos[v] = p + d
                else:
                    if pos[v] != p + d:
                        print("No")
                        exit()
    print("Yes")

main()
