AKIBA = 'AKIHABARA'
s = input()

if s.replace('A', '') != 'KIHBR':
    print('NO')
    exit()
    
t = len(AKIBA)-len(s)
for i in range(len(AKIBA)):
    if i>len(s)-1 or s[i]!=AKIBA[i]:
        s = s[:i]+'A'+s[i:]
    
if s == AKIBA:
    print('YES')
else:
    print('NO')
