S = list(input())

#勝利数
win = S.count("o")
#これから勝つ必要のある試合
korekara = 8 - win
#戦った試合
match = len(S)
#残り試合
nokori = 15 - match

if korekara <= 0:
    print("YES")
elif nokori >= korekara:
    print("YES")
else:
    print("NO")