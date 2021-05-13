s=input()
n=len(s)
f=True
if s[0]!='A':
    f=False
if s[2:n-1].count('C')!=1:
    f=False
for ss in s:
    if ss!='A' and ss!='C' and ss.isupper():
        f=False
print('AC' if f else 'WA')