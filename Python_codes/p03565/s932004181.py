import re

sdash = input().replace('?', '.')
t = input()
len_t = len(t)
isNotUsed = True

for i in range(len(sdash) - len_t, -1, -1):
    if re.match(sdash[i:i+len_t], t):
        s = sdash[:i] + t + sdash[i+len_t:]
        isNotUsed = False
        break
if isNotUsed:
    print('UNRESTORABLE')
else:
    print(s.replace('.', 'a'))