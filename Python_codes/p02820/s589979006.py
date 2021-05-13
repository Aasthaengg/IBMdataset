n,k=map(int,input().split())
s,p,r=map(int,input().split()) #筐体の手に対する勝利ポイント
t=list(input())
ans=0
for i in range(n):
    if t[i]=="s":
        tmp=s
    elif t[i]=="p":
        tmp=p
    else:
        tmp=r
    if i>=k:
        if t[i]==t[i-k]:
            tmp=0
            t[i]=None
    ans+=tmp
print(ans)