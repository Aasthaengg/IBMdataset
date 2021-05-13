S = input()
S_inv = S[::-1]
i=0
flg = True
while i<len(S):
    if S_inv[i:i+5]=='dream'[::-1]:
        i = i + 5
    elif S_inv[i:i+7]=='dreamer'[::-1]:
        i = i + 7
    elif S_inv[i:i+5]=='erase'[::-1]:
        i = i + 5
    elif S_inv[i:i + 6] == 'eraser'[::-1]:
        i = i + 6
    else:
        flg = False
        break

if flg ==True:
    print('YES')
else:
    print('NO')