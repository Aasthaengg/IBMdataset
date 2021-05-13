import sys

global stamp, counter
stamp = {}
counter = 0

def dfs(key, GRAPH):
    global stamp, counter
    if stamp[key][0] == 0:
        counter += 1
        stamp[key][0] = counter
    elif stamp[key][1] != 0:
        return

    for e in GRAPH[key]:
        try:
            if stamp[e][0] == 0:
                dfs(e, GRAPH)
        except:
            pass
    counter += 1
    stamp[key][1] = counter
    return

n = int(raw_input())
x = {}
for i in range(n):
    seq = map(int, raw_input().split())
    key = seq[0]
    if key != 0:
        x[key] = seq[2:]
    else:
        x[key] = []  
    stamp[key] = [0, 0]

for e in x.keys():
    dfs(e, x)

for e in x.keys():
    print e, stamp[e][0], stamp[e][1]