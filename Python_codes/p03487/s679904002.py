import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))

from collections import Counter
c = Counter(a)
ans = 0
for k,v in c.items():
    if k>v:
        ans += v
    elif k<v:
        ans += (v-k)
print(ans)