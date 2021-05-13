
S = input()

S = S[::-1]

cand = {'maerd', 'remaerd', 'esare', 'resare'}

can = True

while S not in cand:
    ok = False
    for x in cand:
        if S[:len(x)] == x:
            S = S[len(x):]
            ok = True
            break
    if ok == False:
        can = False
        break

if can == True:
    print('YES')
else:
    print('NO')