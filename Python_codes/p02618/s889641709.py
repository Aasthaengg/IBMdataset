def calc_score(sch):
    d=[0]*26
    score=0
    for i in range(dur):
        j=sch[i]-1
        s=S[i]
        score+=s[j]+c[j]*(i+1-d[j])+sum([-c[k]*(i+1-d[k]) for k in range(26)])
        d[j]=i+1
    return score

def greedy(dur,c,S,r):
    sch=[]
    d=[0]*26
    for i in range(dur):
        t=0
        s=S[i]
        m=-1<<64
        for j in range(26):
            alt=s[j]+r*c[j]*(i+1-d[j])+sum([-r*c[k]*(i+1-d[k]) for k in range(26)])
            #alt=s[j]-(-c[j]*(i+1-d[j])+sum([c[k]*(i+1-d[k]) for k in range(26)]))**r
            if alt>m:
                m=alt
                t=j
        sch.append(t+1)
        d[t]=i+1
    return sch

dur=int(input())
c=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(dur)]

T=50
a,b=1,8
R=1
tmp=-float('inf')

for r in [a+i*(b-a)/T for i in range(T)]:
    alt_sch=greedy(dur,c,S,r)
    alt=calc_score(alt_sch)
    if tmp<alt:
        tmp=alt
        sch=alt_sch
        R=r

for i in sch:
    print(i)

