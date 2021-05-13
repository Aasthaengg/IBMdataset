from collections import Counter


n, m = map(int, input().split())
a = list(map(int, input().split()))
x = Counter(a)

for i in range(m):
    b, c = map(int, input().split())
    x[c] += b

y = list(zip(x.keys(), x.values()))
y.sort(reverse=True)

ans = 0
k = 0
for z in y:
    if k + z[1] <= n:
        ans += z[0] * z[1]
        k += z[1]
    else:
        ans += z[0] * (n - k)
        k = n
        break
print(ans)
