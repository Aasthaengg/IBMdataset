sstr=list(input())
s=list(map(int,sstr))

op=["" for _ in range(3)]
for i in range(2**3):
    tmp=0
    tmp+=s[0]
    for j in range(3):
        if (i>>j)&1:
            tmp+=s[j+1]
            op[j]="+"
        else:
            tmp-=s[j+1]
            op[j]="-"
    if tmp==7:
        ans=sstr[0]+op[0]+sstr[1]+op[1]+sstr[2]+op[2]+sstr[3]+"=7"
        print(ans)
        break