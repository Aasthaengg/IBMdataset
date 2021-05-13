S = input()
chara0 = S.count('0')
chara1 = S.count('1')
if chara0 < chara1:
    print(chara0 * 2)
else:
    print(chara1 * 2)