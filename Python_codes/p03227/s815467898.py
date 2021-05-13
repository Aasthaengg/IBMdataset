s=list(input())
if(len(s)==3):
    a=s[0]
    s[0]=s[2]
    s[2]=a
print(''.join(s))

