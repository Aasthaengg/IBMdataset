S = input()
while True:
    l = len(S)
    if l == 0:
        print('YES'); break
    if l-5 >= 0 and S[l-5:] == 'dream':
        S = S[:l-5]; continue
    if l-7 >= 0 and S[l-7:] == 'dreamer':
        S = S[:l-7]; continue
    if l-5 >= 0 and S[l-5:] == 'erase':
        S = S[:l-5]; continue
    if l-6 >= 0 and S[l-6:] == 'eraser':
        S = S[:l-6]; continue
    print('NO')
    break