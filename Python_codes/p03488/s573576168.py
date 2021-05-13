from collections import  defaultdict

s = input()
x, y = map(int, input().split())

s_splitted = s.split('T')
x -= len(s_splitted[0])

dist = {0: [], 1: []} # 0: x-direction, 1: y-direction
for i, Fs in enumerate(s_splitted[1:]):
    dist[(i+1) % 2].append(len(Fs))

reachable = {0: set([0]), 1: set([0])}

for i in range(2):
    for d in dist[i]:
        temp = []
        for r in reachable[i]:
            temp.append(r+d)
            temp.append(r-d)
        reachable[i] = set(temp)

if x in reachable[0] and y in reachable[1]:
    print('Yes')
else:
    print('No')