L = list(map(str, input().split(' ')))
que = []
while len(L) != 0:
    if L[0] not in ('+', '-', '*'):
        que.append(int(L.pop(0)))
    else:
        if L[0] == '+':
            a = que[-2] + que[-1]
        elif L[0] == '-':
            a = que[-2] - que[-1]
        elif L[0] == '*':
            a = que[-2] * que[-1]
        L.pop(0)
        que.pop(-1)
        que.pop(-1)
        que.append(a)
print(que[0])
