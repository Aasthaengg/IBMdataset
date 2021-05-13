n, *lst = map(int, open(0).read().split())
lst = sorted([lst[i] - i - 1 for i in range(n)])
res = sum(abs(lst[n // 2] - j) for j in lst)
print(res)
