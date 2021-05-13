s, c = input(), 0
for i in s:
    if i == 'o': c+=1
if c+15-len(s)>=8: print('YES')
else: print('NO')