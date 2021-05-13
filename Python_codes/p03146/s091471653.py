import sys
s = int(input())
m = 1000000
D={} #これで辞書を作る
D[s] = 1
for i in range(2,m):
    if s%2 == 0:
        s = s//2
    else:
        s = 3*s+1
    if s in D.keys(): #sが辞書Dにあるのかチェック(これはある場合)
        D[s] += 1 #D[s] += 1 ->{'s':今までに出てきた回数+1}となる
    else:  #sが辞書Dにない場合
        D[s] = 1 #D[s] = 1 ->{'s':1}となる
    if D[s] ==2:
        print(i)
        sys.exit()