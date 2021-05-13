# coding: utf-8

N = int(input())
S = input()

def kanou(s, i1, i2, i3):
    target = [i1, i2, i3]
    target_iter = target.__iter__()
    now = next(target_iter)
    for c in s:
        if c == now:
            try:
                now = next(target_iter)
            except StopIteration:
                return True
    return False

res = 0
for i in range(0, 1000):
    if i <= 9:
        i1 = "0"
        i2 = "0"
        i3 = str(i)
    elif i <= 99:
        tmp = str(i)
        i1 = "0"
        i2 = tmp[0]
        i3 = tmp[1]
    else:
        tmp = str(i)
        i1 = tmp[0]
        i2 = tmp[1]
        i3 = tmp[2]
    if kanou(S, i1, i2, i3):
        res += 1

print(res)
