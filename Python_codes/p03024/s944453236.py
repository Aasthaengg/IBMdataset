s = input()
rest = 15 - len(s)
print('YES') if list(s).count('o') + rest >= 8 else print('NO')