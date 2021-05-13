s=input()
n=len(s)
if n==4:
    x=s[2]
else:
    x=s[2:n-1]
    
if s[0]!='A':
    print('WA')
    
elif x.count('C')!=1:
    print('WA')
    
else:
    i=x.find('C')
    s=list(s)
    s.pop(i+2)
    s.pop(0)
    s=''.join(s)
    if s.islower()==True:
        print('AC')
    else:
        print('WA')