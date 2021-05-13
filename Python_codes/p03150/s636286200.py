import re
S=input()
keyence = 'keyence'
patterns = []
for i in range(len(keyence)):
    patterns.append('^'+keyence[:i]+'[a-z]*'+keyence[i:]+'$')
for p in patterns:
    if re.match(p,S):
        print('YES')
        exit()
print('NO')