import collections

h, w, n = [int(i) for i in input().split()]
s = [tuple(int(i) for i in input().split()) for j in range(n)]

def dictadd(d, si):
    dc = d
    for i in range(si[0]-2, si[0]+1):
        if 1 <= i <= h-2:
            for j in range(si[1]-2, si[1]+1):
                if 1 <= j <= w-2:
                    dc[(i, j)] += 1
    return dc


d = collections.defaultdict(lambda: 0)
dc = d

for i in s:
    dc = dictadd(dc, i)

dcv = list(dc.values())
ans = []
tot = 0

for i in range(1, 10):
    x = dcv.count(i)
    ans.append(x)
    tot += x

z = (w-2)*(h-2)-tot

print(z)
for i in ans:
    print(i)