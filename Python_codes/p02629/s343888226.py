n = int(input())
chars = 'Xabcdefghijklmnopqrstuvwxyz'
res = ''
while True:
    x = n%26 #最下位の位の文字を求める(係数が26でない最下位の位が余りとして出せる)
    if x == 0: #Xが26のときのみ余り0で対応させるため26に書き換え
        x = 26
    res += chars[x] #文字を正解リストに追加
    n -= x #xを左辺に持っていって右辺で10の位以上の数値を調べる
    if n == 0 :
        break
    n //= 26 #n-xは必ず26の倍数になっている。(xを移項しているから自明)
#最下位の位を余りとして扱うために26で割って係数を消している。
print(res[::-1])#resには1の位が一番初めに入っているので、反転させて表示