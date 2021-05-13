a, b, k = [int(i) for i in input().split()]

lim_1 = min(a + k, b)
lim_2 = max(b - k + 1, a)
ans = set(list(range(a, lim_1)) + list(range(lim_2, b + 1)))

for n in ans:
    print(n)
