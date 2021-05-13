N=int(input())
S=list(input())

ans=0
for i in range(len(S)):
    tmp=0
    a=set(S[:i:])
    b=set(S[i::])
    for i in a:
        if i in b:
            tmp+=1
    ans=max(ans,tmp)
print(ans)