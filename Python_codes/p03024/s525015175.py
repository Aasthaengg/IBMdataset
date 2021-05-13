s = input()

c = 0
for t in s:
    if(t == 'o'):c+=1

if(c >= 8-15+len(s)):print('YES')
else:print('NO')
