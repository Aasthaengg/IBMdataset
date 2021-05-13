import numpy as np

N = int(input())
xy=[]
ans=0

for i in range(N):
    a=int(input())
    xy.append( [list(map(int,input().split())) for _ in range(a)] )

for i in range(2**N):

    # tfに正直フラグを格納
    tf=[0]*N
    for j in range(N):
        if (i>>j)&1:
            tf[j]=1

    # N人分の整合性確認
    marubatu = 1
    for j in range(N):
        # j番目が不親切なら見る意味なし
        if tf[j]==0:
            continue

        # 正しくなかったらtfの組み合わせおかしい　ので次の組み合わせに移る
        for k in range(len(xy[j])):
            if tf[xy[j][k][0]-1]!=xy[j][k][1]:
                marubatu = 0
                break

    if marubatu == 1:
        ans=max(ans,sum(tf))

print(ans)
