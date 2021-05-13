s=input()
ls=len(s)
a=[0]*ls
nr=j=0
for i in range(ls-1):
    if s[i:i+2]=='RL':j=i
    if s[i:i+2]=='LR' or i==ls-2:
        t=''
        if s[i:i+2]=='LR':t=s[nr:i+1]
        elif i==ls-2:t=s[nr:]
        r=t.count('R')
        l=len(t)-r
        a[j+1]+=r//2-(-l//2)
        a[j]+=l//2-(-r//2)
        nr=i+1
print(*a)