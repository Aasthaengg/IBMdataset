# -*- coding: utf-8 -*-
import sys
N=int(sys.stdin.readline().strip())
S=sys.stdin.readline().strip()

ans=0
for d in range(1,N):
    cnt=0
    for s,t in zip(S[d:N],S[:N-d]):
        if s==t:
            cnt+=1
        else:
            ans=max(ans,min(d,cnt)) #最大の文字列一致はd以下
            cnt=0
    else:
        if 0<cnt:   #最後の文字が一致していた場合
            ans=max(ans,min(d,cnt))    #残ったcntも答えの候補になる
print ans