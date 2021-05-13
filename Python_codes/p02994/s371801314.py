n, l = list(map(int, input().split()))
t = []
for i in range(n):
    t.append(l + i)
sum_t = sum(t)
abs_diff = float('inf')
idx = 0
for i in range(n):
    if abs(sum_t - (sum(t[:i]) + sum(t[i + 1:]))) <= abs_diff:
        abs_diff = abs(sum_t - (sum(t[:i]) + sum(t[i + 1:])))
        idx = i
del t[idx]
print(sum(t))
