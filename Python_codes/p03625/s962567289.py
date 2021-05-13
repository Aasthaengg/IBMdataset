from collections import Counter


N = int(input())
A = map(int, input().split())
edge = Counter(A)

cand = [a for a in edge.keys() if edge[a] >= 2]
cand.sort(reverse=True)

e1 = e2 = 0
if len(cand) >= 1:
    if edge[cand[0]] >= 4:
        e1 = e2 = cand[0]
    elif len(cand) > 1:
        e1 = cand[0]
        e2 = cand[1]

print(e1 * e2)
