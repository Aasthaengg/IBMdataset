from collections import Counter

def road_find(a):
    if Road[a] < 0:
        return a
    else:
        return road_find(Road[a])


def train_find(a):
    if Train[a] < 0:
        return a
    else:
        return train_find(Train[a])


def road_union(a, b):
    ag = road_find(a)
    bg = road_find(b)
    if ag == bg:
        return
    if Road[ag] > Road[bg]:
        ag, bg = bg, ag
    Road[ag] += Road[bg]
    Road[bg] = ag
    return


def train_union(a, b):
    ag = train_find(a)
    bg = train_find(b)
    if ag == bg:
        return
    if Train[ag] > Train[bg]:
        ag, bg = bg, ag
    Train[ag] += Train[bg]
    Train[bg] = ag
    return


N, K, L = map(int, input().split())
Road = [-1] * N
Train = [-1] * N

for road in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    road_union(p, q)

for train in range(L):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    train_union(p, q)

Ans = []
for i in range(N):
    Ans.append((road_find(i),train_find(i)))

Ans_C = Counter(Ans)

for i in range(N):
    print(Ans_C[(road_find(i),train_find(i))])

