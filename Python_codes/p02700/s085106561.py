a,b,c,d = map(int, input().split())

for i in range(100): # 繰り返し処理したい、とりあえず100回以上の繰り返しはないから100回繰り返す
    c -= b # 青木くんの体力cから高橋くんの攻撃力bぶん引く
#    print('青木体力', c) # 残り体力を確認する時は先頭の#を外す
    if c <= 0: # 青木くん体力が0以下になったら
        print('Yes') # 高橋くんの勝ちなのでYes
        break # 体力が0になったら繰り返しも終了

    a -= d # 次に高橋くんの体力aから青木くんの攻撃力dを引く
 #   print('高橋体力',a) # 残り体力を確認する時は先頭の#を外す
    if a <= 0: # 高橋くん体力が0以下になったら
        print('No') # 青木くん勝利でNo
        break # 体力が0になったら繰り返しも終了
# どちらの体力も残ってたら次の繰り返し