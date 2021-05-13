def main():
    from bisect import bisect_left
    from bisect import bisect_right
    from sys import stdin
    input=stdin.readline

    n,q=map(int,input().split())
    stx=[list(map(int,input().split())) for _ in [0]*n]
    d=[int(input()) for _ in [0]*q]
    stx=[[s-x,t-x-1,x] for s,t,x in stx]
    stx=[[bisect_left(d,s),bisect_right(d,t),x] for s,t,x in stx]

    #セグ木の要素数（num）および深さ（depth）を計算
    basesize=q
    num,depth=1,1
    while num<basesize:
        num*=2
        depth+=1
    num-=1
    #セグ木を構築
    treesize=num+basesize
    tree=[10**9+1]*treesize
    
    #半開区間[lower,upper)について更新の準備をする関数
    def range_update_pre(lower,upper,new_value):
        q=[[0,1]]  #インデックス、階層
        while q:
            i,f=q.pop()
            #popしたインデックスと階層から、求める下限と上限を算出する
            #幅
            width=pow(2,depth-f)
            #下限と中央と上限
            kagen=(i-pow(2,f-1)+1)*width
            chuo=kagen+width//2
            jogen=kagen+width
            k=2*i+1
            if lower<=kagen and jogen<=upper:
                tree[i]=min(new_value,tree[i])
                continue
            if k<treesize:
                if lower<=kagen and chuo<=upper:tree[k]=min(new_value,tree[k])
                elif lower<=chuo:q.append([k,f+1])
            if k+1<treesize:
                if lower<=chuo and jogen<=upper:tree[k+1]=min(new_value,tree[k+1])
                elif chuo<=upper:q.append([k+1,f+1])

    for s,t,x in stx:
        if s<t:
            range_update_pre(s,t,x)

    for i in range(1,treesize):
        tree[i]=min(tree[i],tree[(i-1)//2])

    ans=[i for i in tree[treesize-basesize:]]
    for i in ans:
        if i==10**9+1:
            print(-1)
        else:
            print(i)
main()