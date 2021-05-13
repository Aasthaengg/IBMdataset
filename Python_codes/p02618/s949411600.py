D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in [0]*D]
k=[]
for i in range(D):
    l=-1
    p=0
    for j in range(26):
        q=s[i][j]-sum([c[a]for a in k])
        p=max([p,q])
        if p==q:
            l=j
    if l==-1:
        l=k[-1]
    k+=[l]
    print(l+1)