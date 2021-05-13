def chk(i):
    print(i)
    return {'Vacant': 0, 'Male': 1, 'Female': -1}[input()]
N = int(input())
l = 0
r = N
sl = chk(l)
if sl:
    while True:
        m = (l+r)//2
        sm = chk(m)
        if sm == 0:
            break
        
        if (sl == sm and (l-m) % 2 == 0) or (sl != sm and (l-m) % 2 == 1):
            l = m
            sl = sm
        else:
            r = m
