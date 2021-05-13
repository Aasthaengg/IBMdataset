#入力
#関数へ
#関数
    #
def a(t,i):
    if i == len(s)-1:
        return sum(map(int,t.split('+')))
    return a(t+s[i+1],i+1) + a(t+'+'+s[i+1],i+1) #関数の中に入れると最後の項でまとめて処理できる
s = input()
print(a(s[0],0))