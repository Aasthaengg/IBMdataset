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
            L-=1
        else:
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
#======================================
N,K=map(int,input().split())
A=list(map(int,input().split()))

def f(x):
    r=0
    for a in A:
        r+=(a+x-1)//x
    return r-N<=K

print(General_Binary_Search(1,max(A),f,Mode=True))