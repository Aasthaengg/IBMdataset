#71d
N = int(input())
Sone = list(input())
Stwo = list(input())

mod_by = 7 + 10**9

#最初のだけ別計算
if Sone[0]==Stwo[0]:
    #ドミノは縦置き
    ans = 3
    before_domino = 1
    i = 1
else:
    #ドミノは横置き
    ans = 6 # 3色*3色-3通り(上下同色)
    before_domino = 0
    i = 2

#前のドミノが縦置き(before_domino=1)の場合
#→今のドミノが縦置きなら2通り
#→今のドミノが横置きなら2通り

#前のドミノが横置き(before_domino=0)の場合
#→今のドミノが縦置きなら1通り
#→今のドミノが横置きなら3通り
    
while i < N:
    if Sone[i] == Stwo[i] and before_domino == 1:
        ans *= 2
        before_domino = 1
        i += 1
    elif Sone[i] != Stwo[i] and before_domino == 1:
        ans *= 2
        before_domino = 0
        i += 2
    elif Sone[i] == Stwo[i] and before_domino == 0:
        ans *= 1
        before_domino = 1
        i += 1
    elif Sone[i] != Stwo[i] and before_domino == 0:
        ans *= 3
        before_domino = 0
        i += 2
        
print(ans%mod_by)