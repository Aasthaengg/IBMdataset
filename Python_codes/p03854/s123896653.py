S = input()

check = ('dream','dreamer','erase','eraser')

index = len(S) + 1
flag = True

while True:
    if len(S) == 0:
        break
    for c in check:
        if S[-len(c):] in check:
            S = S[:-len(c)]
            break
    else:
        flag = False
        break

print('YES' if flag else 'NO')