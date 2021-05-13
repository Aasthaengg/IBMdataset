n, k, s = map(int, input().split())
if s != 10 ** 9:
    print(*[s if i < k else s + 1 for i in range(n)])
else:
    print(*[s if i < k else 1 for i in range(n)])