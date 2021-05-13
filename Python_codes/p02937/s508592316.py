def Binary_Search_Big_Count(A,x,equal=False,sort=False):
    """2分探索によって,xを超える要素の個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"を超える"がx"以上"になる
    """

    if sort:
        A.sort()

    if A[-1]<x or ((not equal) and A[-1]==x):
        return 0

    L,R=-1,len(A)-1
    while R-L>1:
        C=L+(R-L)//2
        if A[C]>x or (equal and A[C]==x):
            R=C
        else:
            L=C
    return len(A)-R

def Binary_Search_High_Value(A,x,equal=False,sort=False):
    """Aのxを超える要素の中で最小のものを出力する.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"を超える"がx"以上"になる
    ※全ての要素がx以上(超える)場合はNoneが返される.
    """

    if sort:
        A.sort()

    K=Binary_Search_Big_Count(A,x,equal=equal,sort=False)
    if K:
        return A[-K]
    else:
        return None
#================================================
S=input()
T=input()

N=len(S)

if not(set(S)>=set(T)):
    print(-1)
    exit()

D={x:[] for x in set(S)}

for i in range(N):
    D[S[i]].append(i)


X=0
A=-1
for t in T:
    P=Binary_Search_High_Value(D[t],A)

    if P==None:
        X+=1
        A=D[t][0]
    else:
        A=P

print(N*X+A+1)