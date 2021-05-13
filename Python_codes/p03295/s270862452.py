(N,M),*ab = [tuple(map(int, s.split())) for s in open(0)]

ab.sort()

max_a = 0
min_b = float('inf')

ans = 1
for i, (a, b) in enumerate(ab):
    if min_b <= a:
        ans += 1
        max_a, min_b = a, b
    else:
        max_a = max(max_a, a)
        min_b = min(min_b, b)

print(ans)