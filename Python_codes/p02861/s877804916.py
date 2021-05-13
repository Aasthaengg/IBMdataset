import math
N = int(input())
XYS = [list(map(int, input().split())) for _ in range(N)]

def rec(prefix, remains):
    if remains:
        for xy in remains:
            for xys in rec(prefix + [xy], [x for x in remains if x != xy]):
                yield xys
    else:
        yield prefix

s = 0
for xys in rec([], XYS):
    prev = xys.pop(0)
    for xy in xys:
        v = math.sqrt(((xy[0] - prev[0])**2) + ((xy[1] - prev[1])**2))
        prev = xy
        s += v

ans = s / math.factorial(N)
print(ans)