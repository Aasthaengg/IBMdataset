
s=list(input())
a=s[0]
b=s[1]
c=s[2]
e=s[3]

for i in range(8):
    d=0
    x=[a,b,c,e]
    for j in range(3):
        if (i >> j)&1:
            x.insert(-j-1-d,'+')
            d+=1
        else:
            x.insert(-1-j-d,'-')
            d+=1
    q="".join(x)
    f=int(a)
    g=int(b)
    h=int(c)
    k=int(e)
    if q[1]=="-":
        g=-g
    if q[3]=="-":
        h=-h
    if q[5]=="-":
        k=-k
    if f+g+h+k==7:
        ans=q+"=7"
        print(ans)
        exit()
    
            
