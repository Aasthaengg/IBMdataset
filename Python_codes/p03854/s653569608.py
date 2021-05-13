S = input()
candidates = ['dream', 'dreamer', 'erase', 'eraser']

while S:
    for candidate in candidates:
        if S.endswith(candidate):
            S = S[:-len(candidate)]
            break
    else:
        break

if S:
    print('NO')
else:
    print('YES')