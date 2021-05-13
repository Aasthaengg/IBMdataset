S = input()
ac = S.count('a')
bc = S.count('b')
cc = len(S)-ac-bc
if abs(ac-bc) <= 1 and abs(ac-cc) <= 1 and abs(bc-cc) <= 1:
    print('YES')
else:
    print('NO')