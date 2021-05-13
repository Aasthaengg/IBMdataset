from math import ceil
a, b = map(int, input().split())

a_min, a_max = ceil(a/0.08), ceil((a+1)/0.08)
b_min, b_max = ceil(b/0.1), ceil((b+1)/0.1)

l = set(range(a_min, a_max)) & set(range(b_min, b_max))
ans = '-1' if len(l) == 0 else min(l)
print(ans)
