S = input()
l = len(S)

if 'keyence' in S:
  print('YES')
  exit()

for i in range(6):
  check = S[:i+1] + S[i+(l-7)+1:]
  if check == 'keyence':
    print('YES')
    exit()
print('NO')
exit()