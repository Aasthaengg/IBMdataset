s = input()
n = len(s)
count_win = s.count('o')
count_trial = 15 - n

if count_trial >= 8 - count_win:
    print('YES')
else:
    print('NO')