S = input()
words = ['dreamer','dream','eraser','erase']
i = len(S)
while i>0:
    update = False
    for w in words:
        if S[:i].endswith(w):
            i -= len(w)
            update =True
            break
    if not update:
        break
print('YES' if i == 0 else 'NO')