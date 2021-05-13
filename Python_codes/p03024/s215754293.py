
#oが勝ち、xが負け
S = input()
le = len(S)

#勝ち数
win = (S.count('o'))

#残試合数
zan = 15 - le

if win + zan >= 8:
  print('YES')
else:
  print('NO')
