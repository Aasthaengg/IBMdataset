a = input()
b = input()
print('YES' if a == b[::-1] and b == a[::-1] else 'NO')
