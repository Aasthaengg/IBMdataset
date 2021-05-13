N = int(input())
S = input()
answer = ""
# アルファベットは26文字,Zの次はAにループするのでoed()で
# UniCode変換後にNを足し、それを%26を行った値を足す
for word in S:
    answer += chr( ord("A") + (ord(word)-ord("A")+N)%26 )

print(answer)

# //////////////////////////////////////////////////
# // ループさせる問題はループの個数の除算分で制御する //
# // 今回はAに,Aと文字の差にずらした分を26で除算する //
# //  ord()←→chr()でそれぞれUniCodeを経て変換可能　 //
# /////////////////////////////////////////////////