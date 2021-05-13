S = input()
X, Y = [int(_) for _ in input().split()]
V = [[0], [0]]
d = 0
f = 1
for s in S:
    if s == 'F':
        if f:
            X -= 1
        else:
            V[d][-1] += 1
    else:
        f = 0
        d = 1 - d
        if V[d][-1]:
            V[d] += [0]
V = [sorted(_) for _ in V]
xs = set()


def judge(diff, vs):
    se = set([0])
    for v in vs:
        sen = set()
        for s in se:
            sen.add(s + v)
            sen.add(s - v)
        se = sen
    if diff not in se:
        print('No')
        exit()


judge(X, V[0])
judge(Y, V[1])
print('Yes')
