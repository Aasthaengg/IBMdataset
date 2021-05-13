from collections import Counter
n,k = map(int,input().split())
a = list(reversed(Counter(map(int,input().split())).most_common()))
if len(a) <= k:
    print(0)
    exit()
s = len(a)-k
ans = 0
for i in range(s):
    ans += a[i][1]
print(ans)