s=list(input())
ans=''
if len(s)==2:
    print(''.join(s))
else:
    tmp=s[0]
    s[0]=s[2]
    s[2]=tmp
    print(''.join(s))