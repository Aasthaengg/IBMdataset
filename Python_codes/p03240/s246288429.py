# -*- coding: utf-8 -*-
n = int(input())
xyh = [list(map(int,input().split())) for i in range(n)]


#全探索すれば良い

#1つめの高さが0ではない情報を記録
for xi,yi,hi in xyh:
    if hi>0:
        memo = [xi,yi,hi]
        break

for cx in range(0,101):
    for cy in range(0,101):
        flg = True
        #cx,cyが中心座標の場合、memoの情報から高さを得られる
        ch = abs(memo[0]-cx)+abs(memo[1]-cy)+memo[2]
        for xi,yi,hi in xyh:
            #各情報の検証
            if hi!=max(ch-abs(xi-cx)-abs(yi-cy),0):
                flg = False
                break
        if flg:
            print("{} {} {}".format(cx,cy,ch))
            import sys
            sys.exit()
