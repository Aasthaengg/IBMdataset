n = input()

sumP = 0

for i in range(2 ** (len(n)- 1)):   #間の数、植木算の全探索
    plus=[]                         #＋位置のリスト
    for j in range(len(n) - 1):     #今調べるやつがどの位置に+をもつか
        if i >> j & 1 :             #iをj回シフトして、0か1を判定する。1なら、そこに+があるため格納したい
            plus.append(j)          

    middle_index = 0

    for pos in plus:
        sumP += int(n[middle_index:pos + 1])       #前半部分を和
        middle_index = pos + 1
    sumP += int(n[middle_index:])                  #後半部分を和

print(sumP)