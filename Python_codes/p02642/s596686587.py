import sys
from collections import Counter

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

s = set()
cnt = Counter(a)

for i in range(n):
    if a[i] in s:
        continue
    if cnt[a[i]] >= 2:
        s.add(a[i])
    for j in range(2,10**6//a[i]+1):
        s.add(a[i]*j)

ans = 0
for i in range(n):
    if a[i] in s:
        continue
    ans += 1

print(ans)
