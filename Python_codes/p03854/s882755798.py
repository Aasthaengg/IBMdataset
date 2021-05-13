S = input()[::-1]
W = ['dream','dreamer','erase','eraser']
i = 0
while i < len(S):
    for w in W:
        if S[i:i+len(w)] == w[::-1]:
            i += len(w)
            break
    else:
        print('NO')
        exit()
print('YES')