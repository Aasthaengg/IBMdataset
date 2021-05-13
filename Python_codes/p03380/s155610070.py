n, *a = map(int, open(0).read().split())
a.sort(reverse=True)
max_a = a[0]
min_diff = float('inf')
for v in a[1:]:
    if abs(max_a/2 - v) <= min_diff:
        ans = v
        min_diff = abs(max_a/2 - v)
print(max_a, ans)