n, k, s = map(int, input().split())
if n <= s:
    m = n - k + 1
    li = [s // m if i != m - 1 else s // m + s % m for i in range(m)]
    for i in range(n):
        if i != n - 1: print(li[i % m], end=' ')
        else: print(li[i % m])
else:
    for i in range(n):
        if i < k: print(s, end=' ')
        elif k <= i < n - 1: print(s + 1, end=' ')
        else: print(s + 1)