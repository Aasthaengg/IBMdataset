s=input()
s_len=len(s)

for i in range(s_len-1):
  for j in range(i,s_len):
    if s[:i]+s[j:]=='keyence':
      print('YES')
      exit()
print('NO')