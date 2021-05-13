S = input()
k = len(S)
win = 0
for i in range(k):
    if S[i] == 'o':
        win = win + 1
if win + 15 - k >= 8:
    print('YES')
else:
    print('NO')
