#13 C - Traveling
N = int(input())

plan = []
for _ in range(N):
    ti,xi,yi = map(int,input().split())
    plan.append((ti,xi,yi))
    
#今いる場所の座標と時間
spot = (0,0,0)#始点
result = 'Yes'
for t,x,y in plan:
    tdiff = t-spot[0]
    xdiff = abs(x-spot[1])
    ydiff = abs(y-spot[2])
    #(x,y)の変化量の和の偶奇と時間の差の偶奇が一致している
    #時間の変化量より(x,y)の変化量の方が小さい
    if (tdiff%2 == (xdiff+ydiff)%2) and ((xdiff + ydiff)<=tdiff):
        '''
        xdiff<=tdiff and ydiff<=t だと(3,3,2)などの範囲外に対応できない
        if (tdiff%2 == (xdiff+ydiff)%2) and (xdiff<=tdiff) and (ydiff<=tdiff):
        '''
        spot = (t,x,y)
    else:
        result = 'No'
        break
print(result)