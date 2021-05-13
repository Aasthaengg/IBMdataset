import re,sys
def S(): return sys.stdin.readline().rstrip()
S = S()
str = 'keyence'
pattern_keyence = []
for i in range(len(str)+1):
    pattern_keyence.append(r'{}'.format(str[:i]+'.*'+str[i:]))
for p in pattern_keyence:
    if re.fullmatch(p,S):
        print('YES')
        break
else:
    print('NO')
