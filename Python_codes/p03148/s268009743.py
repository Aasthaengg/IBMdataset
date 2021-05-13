from operator import itemgetter

N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]

TD.sort(key=itemgetter(1), reverse=True)
selected = TD[:K]
dlc = sum(map(itemgetter(1), selected))
variety = set(map(itemgetter(0), selected))

used = set()
overlap = [] # ダブっているネタの美味しさのリスト
for t, d in TD[:K]:
    if t not in used:
        used.add(t)
    else:
        overlap.append(d)
answer = dlc + len(variety)**2

for t, d in TD[K:]:
    if not overlap:
        break
    if t in used:
        continue
    ov = overlap.pop()
    dlc = dlc - ov + d
    used.add(t)
    answer = max(answer, dlc + len(used)**2)

print(answer)
