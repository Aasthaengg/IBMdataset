# M-SOLUTIONS プロコンオープン: B – Sumo
S = input()

num_win = S.count('o')
print('YES' if 15 - len(S) >= 8 - num_win else 'NO')