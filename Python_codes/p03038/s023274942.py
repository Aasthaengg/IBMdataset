from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
d = Counter(a)

for i in range(m):
    b, c = map(int, input().split())
    d[c] += b
key = list(d.keys())
key.sort(reverse = True)

ans = 0
for k in key:
    if n <= d[k]:
        ans += k*n
        break
    else:
        ans += k*d[k]
        n -= d[k]

print(ans)