S = input()
words = ['dreameraser','dreamerase','dreamer','dream','eraser','erase']
i = 0
while i < len(S):
    update = False
    for w in words:
        if S[i:].startswith(w):
            i += len(w)
            update =True
            break
    if not update:
        break
print('YES' if i == len(S) else 'NO')