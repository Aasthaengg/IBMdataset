a = input()
b = input()

new_str = ''.join(list(reversed(a)))
print('YES' if new_str==b else 'NO')
