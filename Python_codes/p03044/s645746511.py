import collections

n = int(input())
v = []
for i in range(n+10):
    v.append([])

for _ in range(n-1):
    a,b,w = map(int,input().split())
    v[a].append([b,w])
    v[b].append([a,w])

q = collections.deque([])
used = [None] * (n+10)
q.append([1,0])
while len(q) > 0:
    cur, color = q.pop()
    used[cur] = color
    for i in range(len(v[cur])):
        nind, w = v[cur][i]
        if used[nind] != None:
            continue
        if w % 2 == 0:
            q.append([nind, color])
        else:
            q.append([nind, 1-color])
for i in range(1, n+1):
    print(used[i])