##13日後のやつを10日後に
d=int(input())
*c,=map(int, input().split())
s=[]
for _ in range(d):
    *si,=map(int, input().split())
    s.append(si)
last=[-1]*26

ss=0
for i in range(d):
    ind=-1
    smx=-10**10
    for j in range(26):
        ssj=ss+s[i][j]-c[j]*min(10,d-i-1)
        for k in range(26):
            if k!=j:
                ssj-= c[k]*(i-last[k]+min(10,d-i-1))
        if smx<ssj:
            smx=ssj
            ind=j
    last[ind]=i
    ss+=s[i][ind]
    for k in range(26):
        if k!=ind:
            ssj-= c[k]*(i-last[k])
    print(ind+1)






