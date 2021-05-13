n,k=[int(x) for x in input().split()]
p=[int(x)-1 for x in input().split()]
c=[int(x) for x in input().split()]

ans=max(c)
if ans<0:
    print(ans)
    exit()

for i in range(n):
    #最後に自分という順番
    nxt=i
    lp=[]
    while 1:
        nxt=p[nxt]
        lp.append(nxt)
        if nxt==i:
            break
    lpc=max(0,sum(c[x] for x in lp))
    nxt=i
    lpl=len(lp)
    wks=0
    #ループ内の最大値を見る
    for j in range(lpl):
        nxt=p[nxt]
        wks+=c[nxt]
        #ループ内の距離をkから引いた数でループ長を割ることによって
        #剰余部分を加算するパータンと、剰余に突入する1つ前のループの途中でやめた
        #パターンの両方を確認できる
        #ループが負になる場合も考えて,この部分のみ加算するパターンも考える
        #このループはkを超えないので安全
        ans=max(ans,(k-j-1)//lpl*lpc+wks,wks)
        #ループの長さがkを超える場合打ち切る
        if j==k-1:
            break
print(ans)
