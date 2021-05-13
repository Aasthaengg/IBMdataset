S = input()
for i in range(8):
  if S[:i] + S[-7+i:] == 'keyence':
    print('YES')
    quit()

print('NO')