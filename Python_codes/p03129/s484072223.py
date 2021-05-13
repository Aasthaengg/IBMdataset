n, k = map(int, input().split())
if n % 2 == 0:
    res = n // 2
else:
    res = n // 2 + 1
print('YES') if res >= k else print('NO')