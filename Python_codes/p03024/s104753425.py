s = input()
s = s + (15-len(s))*'o'
print('YES' if s.count('o')>7 else 'NO')