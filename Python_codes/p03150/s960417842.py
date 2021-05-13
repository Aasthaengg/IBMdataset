S=input()
t="keyence"
for i in range(1,7):
  if S[:i]==t[:i] and S[-(7-i):]==t[i:]:
    print('YES')
    exit()
    
print('NO')