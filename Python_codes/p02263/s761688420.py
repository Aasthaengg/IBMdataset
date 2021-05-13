data = input().split()
data.reverse()
stk = []

for i in range(len(data)):
    tmp = data.pop()
    if tmp == '+':
        tmp1 = stk.pop()
        tmp2 = stk.pop()
        stk.append(int(tmp2)+int(tmp1))
    elif tmp == '-':
        tmp1 = stk.pop()
        tmp2 = stk.pop()
        stk.append(int(tmp2)-int(tmp1))
    elif tmp == '*':
        tmp1 = stk.pop()
        tmp2 = stk.pop()
        stk.append(int(tmp2) * int(tmp1))
    else:
        stk.append(tmp)

print(stk.pop())