s=list(input())
a=0
t='?'
ch=0
l=len(s)
for i in range(l):
    if ch==1:
        ch=0
        continue
    if s[i]!=t:
        a+=1
        t=s[i]
    else:
        if i<l-1:
            t=s[i]+s[i+1]
            a+=1
            ch=1
print(a)
