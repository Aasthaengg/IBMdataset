N,C = map(int,input().split())
xv = [[0,0]]+[list(map(int,input().split())) for i in range(N)]+[[C,0]]
#0~N+1

#xがある位置
#vがカロリー

#時計回りでの最大値
tokei_maxs = [0]*(N+2)
#時計まわりでの最大値（現状）
tokei=[0]*(N+2)
tokei_max = 0
preans = 0
for i in range(1,N+1,1):
    tmpans = preans + xv[i][1] - (xv[i][0]-xv[i-1][0])
    tokei_max = max(tokei_max,tmpans)
    tokei[i]=tmpans
    tokei_maxs[i]=tokei_max
    preans = tmpans


#h時計回りでの最大値
htokei_maxs = [0]*(N+2)
htokei=[0]*(N+2)
#h時計まわりでの最大値（現状）
htokei_max = 0
preans = 0
for i in range(N,0,-1):
    tmpans = preans + xv[i][1] - (xv[i+1][0]-xv[i][0])
    htokei_max = max(htokei_max,tmpans)
    htokei_maxs[i]=htokei_max
    htokei[i]=tmpans
    preans=tmpans

ans = max(max(tokei),max(htokei))

for i in range(0,N+1,1):
    ans = max(ans,tokei[i]+htokei_maxs[i+1]-xv[i][0])
for i in range(N+1,0,-1):
    ans = max(ans,htokei[i]+tokei_maxs[i-1]-C+xv[i][0])

print(ans)

