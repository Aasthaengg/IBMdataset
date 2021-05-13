#==========================================================
def General_Binary_Search(L,R,cond,Mode=True,Integer=True,ep=1/(1<<20)):
    """一般的な二部探索を行う.
    L:解の下限
    R:解の上限
    cond:条件(1変数関数,広義単調減少 or 広義単調減少を満たす)
    Mode:True->広義単調増加,False->広義単調減少
    Integer:解を整数に制限するか?
    ep:Integer=Falseのとき,解の許容する誤差
    """

    if Integer:
        if Mode:
            if not cond(R):
                return R+1
            L-=1
        else:
            if not cond(L):
                return L-1
            R+=1

        while R-L>1:
            C=L+(R-L)//2
            if cond(C)^Mode:
                L=C
            else:
                R=C
        if Mode:
            return R
        else:
            return L
    else:
        C=L+(R-L)/2
        while (R-C)>ep:
            if cond(C)^Mode:
                L=C
            else:
                R=C
            C=L+(R-L)/2
        return C
#==========================================================
def g(x):
    S=A[x]
    for i in range(N):
        if i!=x:
            if A[i]<=2*S:
                S+=A[i]
            else:
                return False
    return True
#==========================================================
N=int(input())
A=list(map(int,input().split()))

A.sort()

if not g(N-1):
    print(0)
elif g(0):
    print(N)
else:
    print(N-General_Binary_Search(0,N-1,g,True))