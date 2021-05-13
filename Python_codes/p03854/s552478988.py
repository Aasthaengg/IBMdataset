S = input()
li = ['dream','dreamer','erase','eraser']
li_len=[5,7,5,6]

while S:
    for i,moji in enumerate(li):
        if S[-li_len[i]:] == moji:
            S = S[:-li_len[i]]
            break
    else:
        print('NO')
        break
if not S:print('YES')
