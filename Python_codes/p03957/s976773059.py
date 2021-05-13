#%%
s = list(input())

f1 = False
f2 = False

for i in range(len(s)):
    if s[i] == 'C':
        f1 = True
    if f1 and s[i] == 'F':
        f2 = True
if f1 and f2:
    print('Yes')
else:
    print('No')
