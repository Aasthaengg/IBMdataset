S = input()
SFlag = True
while S:
    if S[-7:]=='dreamer':
        S = S[:-7]
    elif S[-6:]=='eraser':
        S = S[:-6]
    elif S[-5:]=='dream' or S[-5:]=='erase':
        S = S[:-5]
    else:
        SFlag = False
        break
print(['NO','YES'][SFlag])