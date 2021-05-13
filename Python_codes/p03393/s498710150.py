S=list(input())
N=len(S)
abc=list("abcdefghijklmnopqrstuvwxyz")
D={}
for a in abc:
    D[a]=0
idx={}
for i in range(26):
    idx[abc[i]]=i

for s in S:
    D[s]+=1
L=[]
for k,v in D.items():
    if v==0:
        L.append(k)

L=sorted(L)
if len(L)==0:
    lis=[]
    for i in range(25,-1,-1):
        s=S[i]
        lis.append(s)
        if i!=0:
            if idx[s]>idx[S[i-1]]:
                break
    if len(lis)==26:
        print(-1)
        exit()

    lis=sorted(lis)
    for l in lis:
        if idx[S[i-1]]<idx[l]:
            add=l
            break
    ans="".join(S[:i-1])+add
    print(ans)

        
else:
    print("".join(S)+L[0])
#yzxwvutsrqponmlkjihgfedcba