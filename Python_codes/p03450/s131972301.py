import sys
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 複数回出てきているところが問題、グラフ問題として連結した部分で判定
N, M = lr()
adjacent = [[] for _ in range(N+1)] # 1-indexed
for _ in range(M):
    l, r, d = lr()
    adjacent[l].append((r, d))
    adjacent[r].append((l, -d))

X = [None] * (N+1)
used = set()

def check(i):
    global used
    used.add(i)
    if X[i] == None: X[i] = 0
    for target, dist in adjacent[i]:
        if X[target] != None and X[target] != X[i] + dist:
            print('No')
            exit()
        if target in used:
            continue
        else:
            X[target] = X[i] + dist
            check(target)

for i in range(1, N+1):
    check(i)

print('Yes')
# 54