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
    news=[s[d][i]-c[i]*((d+10)-last[i])*((d+10)-last[i]-1)//2 for i in range(26)]
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

for i in dt:
    print(i)