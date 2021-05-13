import re
s = input()
t = input()

s= s.replace('?','.')

n_s = len(s)
n_t = len(t)

res = []

for i in range(n_s-n_t+1):
    m = re.match(s[i:i+n_t],t)
    if not m:continue
    res.append((s[:i]+t+s[i+n_t:]).replace('.','a'))
if not res:
    print('UNRESTORABLE')
else:
    print(min(res))