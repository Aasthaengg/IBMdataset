seq = input().split()

stk = []
opr = ['+', '-', '*']

for e in seq:
    if e in opr:
        if e == '+':
            res = stk[-2] + stk[-1]
        elif e == '-':
            res = stk[-2] - stk[-1]
        elif e == '*':
            res = stk[-2] * stk[-1]
        stk = stk[:-2] + [res]
    else:
        stk.append(int(e))

print(stk[0])

