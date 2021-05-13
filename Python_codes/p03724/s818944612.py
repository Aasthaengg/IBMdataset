import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


from collections import defaultdict
n,m = map(int, input().split())
ns = defaultdict(int)
for _ in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u] += 1
    ns[v] += 1
if all(val%2==0 for val in ns.values()):
    ans = "YES"
else:
    ans = "NO"
print(ans)