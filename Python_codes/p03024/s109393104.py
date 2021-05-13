s = input()
a = s.count('o')
print('YES' if a + 15-len(s) >= 8 else 'NO')