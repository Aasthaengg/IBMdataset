n = int(input())
xss = [[int(x)-1 for x in input().split()] for _ in range(n)]

def solve(n, xss):
    yss = [[-1] + list(reversed(xs)) for xs in xss]
    ans = 0
    candidates = range(n)
    while True:
        #print(" ".join(map(str, candidates)))
        ms = list(matches(yss, candidates))
        if len(ms) == 0:
            if all(len(ys)==1 for ys in yss):
                return ans
            else:
                return -1
        ans += 1
        candidates = []
        #print(" ".join(map(str, ms)))
        for x, y in ms:
            yss[x].pop()
            yss[y].pop()
            candidates.append(x)
            candidates.append(y)

def matches(yss, candidates):
    firsts = [yss[i][-1] for i in candidates]
    ans = set()
    for x, y in zip(candidates, firsts):
        if y!=-1 and yss[y][-1] ==x:
            ans.add((min(x, y), max(x, y)))
    return ans

print(solve(n, xss))