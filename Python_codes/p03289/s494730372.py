s = input()

c=0
ok = True
if s[0]!='A':
    ok = False
else:
    for i in range(len(s)):
        if s[i]=='C' and i in range(2,len(s)-1):
            if c==0:
                c=i
            else:
                ok = False
    if c==0:
        ok=False
    else:
        s = s.replace('A','').replace('C','')
        if s!=s.lower():
            ok=False
            
if ok:
    print('AC')
else:
    print('WA')