h, w, n = map(int, input().split())
lst = []
for i in range(n):
    ai, bi = map(int, input().split())
    lst.append((ai, bi))

dic = {}
for i in range(10): dic[i] = 0
dic[0] = (h-2) * (w-2)
already = set([])
idx = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(n):
    ai, bi = lst[i]
    for surround in idx:
        center = [ai+surround[0], bi+surround[1]]
        if min(center) < 2 or center[0] > h-1 or center[1] > w-1: continue
        cnt = 0
        for ind in idx:
            cell = (center[0]+ind[0], center[1]+ind[1])
            if cell in already: cnt += 1
        dic[cnt] -= 1
        dic[cnt+1] += 1
    already.add((ai, bi))

for i in range(10):
    print(dic[i])