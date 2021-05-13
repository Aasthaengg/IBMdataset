N=int(input())
A=list(map(int,input().split()))
d={}
dd={}
if len(A)==1:
    if A[0]==1:
        print(0)
    else:
        print(1)
else:
    for a in A:
        try:
            d[a]+=1
            dd[a]+=1
        except KeyError:
            d[a]=1
            dd[a]=1
        #揃ったら除くべき数値を初期化
        if dd[a]==a:
            d[a]=0
    print(sum(d.values()))