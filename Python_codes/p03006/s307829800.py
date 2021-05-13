from collections import Counter
N=int(input())
balls=[tuple(map(int, input().split())) for _ in range(N)]

#2ボールの相対座標をぜんぶ調べる
R=[(x[0]-y[0],x[1]-y[1]) for x in balls for y in balls]
C=Counter(R).most_common()

#いちばん多い相対座標を(p,q)とする
#C[0]は(0,0)なので除外
if len(C)<=1:
    print(N)
else:
    print(N-(C[1][1]))