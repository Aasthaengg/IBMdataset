D=int(input())
*c,=map(int,input().split())
s=[]
for i in range(D):
    *x,=map(int,input().split())
    s.append(x)

dt=[]
last=[-1]*26
v=0
for d in range(D):
    news=[s[d][i]+c[i]*(d-last[i])*(d-last[i]-1) for i in range(26)]
    maxi=0
    tmp=-float('inf')
    for i in range(26):
        if tmp<news[i]:
            maxi=i
            tmp=news[i]
    last[maxi]=d
    v+=s[d][maxi]
    for i in range(26):
        v-=c[i]*(d-last[i])
    dt.append(maxi+1)

def score(T):
    last=[-1]*26
    v=0
    for d in range(D):
        v+=s[d][T[d]-1]
        last[T[d]-1]=d
        for i in range(26):
            v-=c[i]*(d-last[i])
    return v

v0=max(score(dt)+10**6,0)

for _ in range(6):
    for d in range(1,D):
        y=-1
        newdt=dt+[]
        for i in range(26):
            if dt[d]!=i+1:
                newdt[d]=i+1
                v1=max(score(newdt)+10**6,0)
                if v0<v1:
                    y=i+1
                    v0=v1
        if y!=-1:
            dt[d]=y

for i in dt:
    print(i)