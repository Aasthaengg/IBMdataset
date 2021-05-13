A,B,C,D,E,F=list(map(int,input().split()))

answ=1
anss=0

for b in range(F//(100*B)+1):
    for a in range((F-100*B*b)//(100*A)+1):
        w=100*A*a+100*B*b
        if w==0:
            continue
        smax=min(F-w,w*E//100)
        s=0
        for d in range(smax//D+1):
            c=(smax-d*D)//C
            tmps=c*C+d*D

            s=max(s,tmps)

        if anss*(s+w)<=s*(anss+answ):
            answ=w
            anss=s

print('{} {}'.format(answ+anss,anss))