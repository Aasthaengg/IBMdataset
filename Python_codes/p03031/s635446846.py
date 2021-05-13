# C - Switches
#bit全探索の練習問題
import copy

N,M = input().split()
N = int(N)
M = int(M)

ks = []
for l in range(M):
    s = input().split()
    ks.append(s)
p = list(map(int, input().split()))

KS = []
for m in range(M):#列の数はМ
    box = list()
    for n in range(len(ks[m])):#M列の要素を数字に直す処理
        ks[m][n] = int(ks[m][n])
        box.append(ks[m][n])
    KS.append(box)            

swich = []
for o in range(M):#列の数はМ
    swi = list()
    for r in range(1,len(KS[o])):#k以外を取り出す
        swi.append(ks[o][r])
    swich.append(swi)
           
ans = 0
for i in range(1<<N):#全パターンは2**(スイッチの総数)
    SWICH = copy.deepcopy(swich)
    light_on = 0
    for j in range(N):
        mask = 1<< j#1をj個左にずらした2進数
        if i & mask != 0:#スイッチjがonの時
            continue
        else:#スイッチjがoffの時
            for y in range(M):#電球iごとに繰り返し
                if (j+1 in SWICH[y]) == True:#スイッチsiが電球iに接続されているとき
                    SWICH[y].remove(j+1)

    #onのみがSWICHに入っている
    flat_SWICH = []
    for a in range(len(SWICH)):
        for b in range(len(SWICH[a])):
            flat_SWICH.append(SWICH[a][b])
            
    for x in range(M):
        if (len(SWICH[x]) % 2) == p[x]:#onのスイッチの数を2で割った余りがPの値と等しい時
            light_on += 1
    if light_on == M:#onの電球の個数がMと等しい(全てon)時
        ans += 1
print(ans)