import re
s = str(input())
n = len(s)
z = [0] * n
lr = [m.start() for m in re.finditer('LR', s)]
rl = [m.start() for m in re.finditer('RL', s)]
t = []
if lr == []:
    t.append(s)
else:
    t.append(s[:lr[0]+1])
    for i in range(len(lr)-1):
        t.append(s[lr[i]+1 : lr[i+1]+1])
    t.append(s[lr[-1]+1:])
for i in range(len(t)):
    r = t[i].count('R')
    l = len(t[i]) - r
    # x : RL界面左側の数。y : RL界面右側の数。
    x = (r+1) // 2 + l // 2
    y = r // 2 + (l+1) // 2
    z[rl[i]] = x
    z[rl[i]+1] = y

delta = [str(i) for i in z]
ans = ' '.join(delta)
print(ans)