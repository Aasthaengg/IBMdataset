N=int(input())
S=[list(map(str,input().split())) for _ in range(N)]
for row in S:
    row[1]=int(row[1])
SS=sorted(S)
ins=0
ans=list()
tmp=0
for i in SS:
    if i[0]==tmp:
        ans.insert(ins,i)
    else:
        ins=len(ans)
        ans.append(i)
        tmp=i[0]
for j in ans:
    print(S.index(j)+1)