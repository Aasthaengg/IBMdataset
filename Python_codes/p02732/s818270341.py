from collections import Counter
n = int(input())
a = list(map(int, input().split()))

d = Counter(a)
key = d.keys()
ans = 0
for i in key:
    ans += (d[i]*(d[i]  - 1))//2

for i in a:
    print(ans - d[i] + 1)