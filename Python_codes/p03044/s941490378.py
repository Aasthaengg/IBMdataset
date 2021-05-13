import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
from collections import defaultdict
ns = defaultdict(set)
for i in range(n-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    ns[u].add((w, v))
    ns[v].add((w, u))
    
q = [(0,0)]
ans = [None]*n
ans[0] = 0
while q:
    d,u = q.pop()
    for w,v in ns[u]:
        if ans[v] is None:
            val = (w+d)%2
            q.append((val, v))
            ans[v] = val
write("\n".join(map(str, ans)))