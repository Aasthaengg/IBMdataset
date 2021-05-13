from sys import exit

S = input()

min_win = len(S) - 7

win_count = 0

for s in S:
    if s == 'o':
        win_count += 1

if win_count >= min_win:
    print('YES')
else:
    print('NO')
