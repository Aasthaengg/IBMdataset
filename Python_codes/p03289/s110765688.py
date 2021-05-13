s = input()
n = len(s)
ok = True
if s[0] != 'A': ok = False
c_counter = 0
p = -1
for i in range(2,n-1):
    if s[i] == 'C':
        c_counter += 1
        p = i
if c_counter != 1: ok = False
if ok == 0: 
    print('WA')
    exit()
for i in range(n):
    if i == 0 or i == p: continue
    if ord(s[i]) < 97: ok = False
if ok: print('AC')
else: print('WA')
