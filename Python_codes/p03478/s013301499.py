# coding= utf-8
abN=input("")
nab=abN.split(" ")
rn=int(nab[0])
ra=int(nab[1])
rb=int(nab[2])
p=[int(s+1) for s in range(rn)]
def counting(s):
    if s<10:
        if ra<=s<=rb:
            return s
    if 10<=s<100:
        s=str(s)
        w10=int(s[0:1])
        w1=int(s[1:2])
        s=int(s)
        ww=w10+w1
        if ra<=ww<=rb:
            return s
    if 100<=s<1000:
        s=str(s)
        w100=int(s[0:1])
        w10=int(s[1:2])
        w1=int(s[2:3])
        s=int(s)
        ww=w100+w10+w1
        if ra<=ww<=rb:
            return s
    if 1000<=s<10000:
        s=str(s)
        w1000=int(s[0:1])
        w100=int(s[1:2])
        w10=int(s[2:3])
        w1=int(s[3:4])
        s=int(s)
        ww=w1000+w100+w10+w1
        if ra<=ww<=rb:
            return s
    if 10000==s:
        if ra<=1<=rb:
            return s
    else:
        return 0
r=map(counting,p)
g=list(r)
print(sum(g))