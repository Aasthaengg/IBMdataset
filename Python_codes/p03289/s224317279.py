s=list(input())
flag=1
if s[0]!='A':
    flag=0
if 'C' not in s[2:-1]:
    flag=0
if s.count('C')!=1:
    flag=0
if 'A' in s:
    s.remove('A')
if 'C' in s:
    s.remove('C')
s=''.join(s)
if s.islower():
    pass
else:
    flag=0
if flag==1:
    print('AC')
else:
    print('WA')