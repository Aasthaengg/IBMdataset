# 各秒数を取得
X,t = map(int,input().split())
 
#残りの砂を計算し出力
Remain = X - t
if Remain > 0:
    print(Remain)
else:
    print("0")