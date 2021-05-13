
n, m = map(int, input().split())
h = list(map(int, input().split()))

good = 0

obs = [[] for i in range(n) ]

for i in range(m):
    a, b = map(int, input().split())
    obs[a-1].append(b)
    obs[b-1].append(a)

for idx,o in enumerate(obs):
    higher = True
    if len(o) == 0:
        good += 1
        continue
    o = set(o)
    for i in o:
        if h[idx] <= h[i-1]:
            higher = False
    if higher:
        good += 1

print(good)