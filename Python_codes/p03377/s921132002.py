a, b, x = map(int, input().split())
print('YES' if a==x or a+b>=x and a<=x else 'NO')