A,B,C,D,E,F=map(int,input().split())
w=set()
s=set()
sw=0
sws=0
sww=0
for i in range(F//(100)):
    for j in range(F//(100)):
        w.add(i*100*A+j*100*B)
for i in range(F//C):
    for j in range(F//D):
        s.add(i*C+j*D)
s=list(s)
w=list(w)
for i in range(len(w)):
    for j in range(len(s)):
        if w[i]+s[j]!=0:
            tmp=(s[j]*100)/(w[i]+s[j])
            if sw <= tmp <= (E*100)/(100+E) and F >= w[i]+s[j]:
                sw =tmp
                sww= w[i]+s[j]
                sws = s[j]
print(sww,sws)