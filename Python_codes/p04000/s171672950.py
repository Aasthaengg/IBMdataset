h, w, n = map(int, input().split())
a = {tuple(map(int, input().split())) for _ in range(n)}

d = {}
c = [0] * 10

def next(x, y):
    ret = []
    for i in range(max(0, x-2), min(h-2, x+1)):
        for j in range(max(0, y-2), min(w-2, y+1)):
            ret.append((i, j))
    return ret

for x, y in a:
    x -= 1
    y -= 1
    for s, t in next(x, y):
        if (s, t) not in d:
            count = 0
            for i in range(3):
                for j in range(3):
                    if (s + i + 1, t + j + 1) in a:
                        count += 1
            d[(s, t)] = count
            c[count] += 1

c[0] = (h-2) * (w-2) - sum(c)

for x in c:
    print(x)