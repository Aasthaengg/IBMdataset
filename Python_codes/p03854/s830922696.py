S = input()

idx = len(S)
while True:
    if S[idx-5:idx] == 'dream':
        idx -= 5
    elif S[idx-6:idx] == 'eraser':
        idx -= 6
    elif S[idx-5:idx] == 'erase':
        idx -= 5
    elif S[idx-7:idx] == 'dreamer':
        idx -= 7
    else:
        print('NO')
        break

    if idx == 0:
        print('YES')
        break
