def Binary_Search_Small_Count(A,x,sort=True,equal=False):
    """2分探索によって,x未満の要素の個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"未満"がx"以下"になる
    """
    if sort:
        A.sort()
        
    N=len(A)
    if A[-1]<x:
        return N
    elif x<A[0] or (not equal and x==A[0]):
        return 0

    L,R=0,N
    while R-L>1:
        C=L+(R-L)//2
        if x<A[C] or (not equal and x==A[C]):
            R=C
        else:
            L=C
    return R
#=======================================
N=int(input())
L=list(map(lambda x:int(x),input().split()))
inf=float("inf")

T={}
for i in range(N):
    x=L[i]
    if x in T:
        T[x]+=1
    else:
        T[x]=0
        
    L[i]=(x,T[L[i]])
L.sort()

D=0
for i in range(N):
    (b,y)=L[i]
    for j in range(i+1,N):
        (c,z)=L[j]

        X=Binary_Search_Small_Count(L,(b,y),False,False)
        Y=Binary_Search_Small_Count(L,(c-b,inf),False,True)

        D+=max(0,X-Y)
print(D)
