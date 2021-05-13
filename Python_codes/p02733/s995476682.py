# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

H,W,K=map(int, sys.stdin.readline().split())
S=[ sys.stdin.readline().strip() for _ in range(H) ]

ans=float("inf")
for bit in range(2**H):
    cnt=0
    group_num=0
    GROUP={}
    for i,s in enumerate(S):
        if i==0:
            GROUP[i]=group_num
        else:
            if bit>>i-1&1==1:
                cnt+=1      #境目のカウントに+1
                group_num+=1
            GROUP[i]=group_num

    ok=None
    VALUE=defaultdict(lambda: 0)
    w=0
    break_flag=False
    for w in range(W):
        if break_flag:  #breakフラグがTrueならループを止める
            break
        for h in range(H):
            VALUE[GROUP[h]]+=int(S[h][w])
        #現時点の集計でKを超えている値がないかをチェック
        for v in VALUE.values():
            if v<=K:
                pass
            else:
                if ok is None:      #okに値がない場合は、このパターンは成り立たない
                    cnt=float("inf")    #不可能なパターンなのでカウントに無限大を代入
                    break_flag=True     #breakフラグにTrueを代入
                    break
                else:      #以前の列でok番号に値が入っていた、つまり成り立つ列があった場合
                    cnt+=1      #境目のカウントに+1
                    VALUE=defaultdict(lambda: 0)    #NGの場合は値を初期化して入れなおし
                    for h in range(H):
                        VALUE[GROUP[h]]+=int(S[h][w])
                    break
        else:
            ok=w    #値が全てK以下だった場合はok変数に列番号を記録
    ans=min(ans,cnt)
       
print ans