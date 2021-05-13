import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


from collections import defaultdict
n = int(input())
ns = defaultdict(set)
uvs = [None]*(n-1)
for i in range(n-1):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add(v)
    ns[v].add(u)
    uvs[i] = (u,v)
c = list(map(int, input().split()))
c.sort()
q = [0]
ans = [None]*n
i = 0
def sub(u, prev):
    global i
    for v in ns[u]:
        if prev==v:
            continue
        sub(v, u)
    ans[u] = c[i]
    i += 1
sub(0, -1)
val = 0
for u,v in uvs:
    val += min(ans[u], ans[v])
print(val)
write(" ".join(map(str, ans)))