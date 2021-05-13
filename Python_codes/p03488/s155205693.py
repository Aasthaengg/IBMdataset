order = list(input())
X, Y = map(int, input().split())
 
Xs = []
Ys = []
cnt = 0
now_lis = Xs
x_dir = 1
for s in order:
    if s=='T':
        if not cnt==0:
            now_lis.append(cnt)
        now_lis = Ys if x_dir else Xs
        x_dir = not x_dir
        cnt = 0
    else:
        cnt += 1
if not cnt==0:
    now_lis.append(cnt)

if order[0]=='T':
    x_start = 0
else:
    x_start = Xs[0]
    del Xs[0]

def dp(start, lis, goal):
    nodes = set([start])
    for x in lis:
        nx = set()
        L = list(nodes)
        for l in L:
            nx.add(l+x)
            nx.add(l-x)
        nodes = nx
    return goal in nodes
 
if dp(x_start, Xs, X) and dp(0, Ys, Y):
    print('Yes')
else:
    print('No')