def check(arr, x):
    pos = set([0])
    for dx in arr:
        npos = set()
        for p in pos:
            npos.add(p+dx)
            npos.add(p-dx)
        pos = npos
    return x in pos


s = input().split('T')
x, y = map(int, input().split())
d = [len(ss) for ss in s]
dx = d[2::2]
dy = d[1::2]
x -= d[0]
if check(dx, x) and check(dy, y):
    print('Yes')
else:
    print('No')
