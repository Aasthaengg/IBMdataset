import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

from collections import defaultdict
rows, cols = map(int, input().split())
n = rows*cols
ns = defaultdict(set)
ss = [None] * rows
color = [None] * n
for i in range(rows):
    s = input()
    ss[i] = s
    for j,c in enumerate(s):
        u = i*cols+j
        color[u] = c
        if i>0:
            if c!=ss[i-1][j]:
                v = u - cols
                ns[u].add(v)
                ns[v].add(u)
        if j>0:
            if c!=s[j-1]:
                v = u - 1
                ns[u].add(v)
                ns[v].add(u)
seen = [False] * n
ans = 0
for u in range(n):
    if seen[u]:
        continue
    q = [u]
    s = set([u])
    while q:
        u = q.pop()
        for v in ns[u]:
            if seen[v]:
                continue
            seen[v] = True
            s.add(v)
            q.append(v)
    ans += sum(color[item]=="#" for item in s) * sum(color[item]=="." for item in s)
print(ans)