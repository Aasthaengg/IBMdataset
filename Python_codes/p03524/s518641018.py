S = input()

Slst = [S.count('a'), S.count('b'), S.count('c')]
Slst.sort(reverse=True)

x = (len(S)-1) // 3
y = (len(S)-1) % 3
if y == 0:
    lst = [x+1, x, x]
elif y == 1:
    lst = [x + 1, x+1, x]
else:
    lst = [x+1, x+1, x+1]
if lst == Slst:
    print('YES')
else:
    print('NO')