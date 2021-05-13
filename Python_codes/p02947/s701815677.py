import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
ss = [input() for _ in range(n)]
count = []
l = [chr(v) for v in range(ord("a"), ord("z")+1)]
d = {c:i for i,c in enumerate(l)}
for s in ss:
    val = [0]*26
    for c in s:
        val[d[c]] += 1
    count.append(tuple(val))
from collections import Counter
c = Counter(count)
ans = sum(v*(v-1)//2 for v in c.values())
print(ans)