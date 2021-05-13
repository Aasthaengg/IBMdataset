N, K = map(int,input().split())
#N以下の数でKの倍数の個数(mod K で0と等しいものの個数)
cntMod = N//K
#Kが奇数のときは3つ組として(0,0,0)しかとれない　ただしmod K
#Kが偶数のときは3つ組として(K/2,K/2,0)もとれる ただし　mod K
if K%2==0:
    if K*cntMod+K//2 <= N:
        cntMid = cntMod + 1
    else:
        cntMid = cntMod
else:
    cntMid = 0
print(cntMid**3+cntMod**3)
