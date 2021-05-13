n, t = map(int, input().split())
a = list(map(int, input().split()))

ans = []
min_a = a[0]
for i in range(1, n):
    min_a = min(min_a, a[i-1])
    ans.append(a[i] - min_a)
r = max(ans)
print(ans.count(r))
