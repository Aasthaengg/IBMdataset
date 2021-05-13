s,f=input()[::-1],-1
while f<0:
    if s:
        if s[:5]=='maerd':
            s=s[5:]
        elif s[:5]=='esare':
            s=s[5:]
        elif s[:6]=='resare':
            s=s[6:]
        elif s[:7]=='remaerd':
            s=s[7:]
        else:
            f=0
    else:
        f=1
print(['NO','YES'][f])