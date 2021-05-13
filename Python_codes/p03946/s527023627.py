import sys
readline = sys.stdin.buffer.readline

n,t = map(int,readline().split())
lst1 = list(map(int,readline().split()))
counter = []
mn = 10**9+1

for i in range(n):
    if lst1[i] < mn:
        mn = lst1[i]
    if mn < lst1[i]:
        counter.append(lst1[i]-mn)

from collections import Counter
c = Counter(counter)

ans = 0
mx = 0
for key,value in c.items():
    if key > mx:
        ans = value
        mx = key

print(ans)