H, W, M = map(int, input().split())
hws = [list(map(lambda x :int(x)-1, input().split())) for _ in range(M)]

booms = [set() for _ in range(H)]

yoko = [0 for _ in range(W)]
tate = [0 for _ in range(H)]

for hw in hws:
    tate[hw[0]] += 1
    yoko[hw[1]] += 1
    booms[hw[0]].add(hw[1])
    
max_tate = max(tate)
max_yoko = max(yoko)


tate_candidates = []
yoko_candidates = []

for i in range(H):
    if tate[i] == max_tate:
        tate_candidates.append(i)
        
for i in range(W):
    if yoko[i] == max_yoko:
        yoko_candidates.append(i)

exist = 0
for tate_candidate in tate_candidates:
    for yoko_candidate in yoko_candidates:
        if yoko_candidate not in booms[tate_candidate]:
            exist = 1
            break
    else:
        continue
    break
print(max_tate + max_yoko + (exist-1))
