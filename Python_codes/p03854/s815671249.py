S = input()
T = ['dream','dreamer','erase','eraser']
while len(S) != 0:
    for t in T:
        if S.endswith(t):
            S = S[:len(S)-len(t)]
            break
    else:
        print('NO')
        exit()
print('YES')