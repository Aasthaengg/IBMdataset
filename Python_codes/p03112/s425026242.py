# 各クエリに対して,二分探索で解を求める

def bs(x,li):
    # 値xがliの2連続した値a,b達が作る[a,b)のどこに入るか
    # aを返す
    # liはソート済みとする
    left,right=0,len(li)
    while left+1<right:
        mid = (left+right)//2
        if li[mid]<=x:
            left=mid
        else:
            right=mid
    return left

def get(L):
    ret=[-10**13]
    for _ in range(L):
        ret.append(int(input()))
    ret.append(10**13)
    return ret

A,B,Q=map(int,input().split())
S=get(A)
T=get(B)
for _ in range(Q):
    x=int(input())

    # sn,sp,tn,tpを二分探索で出す
    sn,tn=bs(x,S),bs(x,T)

    # これらの経路の組み合わせの中に最小値が含まれている
    # 全部で8パターンあるので全探索してminをansとして保持
    ans=10**13
    for s in [S[sn],S[sn+1]]:
        for t in [T[tn],T[tn+1]]:
            d=abs(s-x)+abs(t-s)
            e=abs(t-x)+abs(s-t)
            ans=min([ans,d,e])
    print(ans)