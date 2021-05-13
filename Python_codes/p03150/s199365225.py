S = input()
n = len(S) - 7
for i in range(n, len(S)):
  if S[:i - n] + S[i:] == 'keyence':
    print('YES')
    exit()
    
print('NO')