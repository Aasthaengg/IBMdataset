import itertools

s = input()
x,y = map(int,input().split())
d = [len(fs) for fs in s.split('T')]
x -= d[0]
dx = d[2::2]
dy = d[1::2]

def check(d,x):
    set_ = set([0])
    for dx in d:
        set_ = {a+b for a,b in itertools.product(set_,[dx,-dx])}
    return x in set_
if check(dx,x) and check(dy,y):
    print('Yes')
else:
    print('No')