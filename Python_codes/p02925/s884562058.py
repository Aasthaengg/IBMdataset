from collections import deque
n = int(input())
a = []
for i in range(n):
    a1 = list(map(int,input().split()))
    a.append(a1)
l = [[[] for i in range(n)] for i in range(n)]
c = 0
day = 0
for i in range(n):
    ap = [i,a[i][0]-1]
    ap.sort()
    for j in range(1,n-1):
        p = [i,a[i][j]-1]
        p.sort()
        l[ap[0]][ap[1]].append(p)
        ap = p
rl = [[0 for i in range(n)] for i in range(n)]
dl = [[0 for i in range(n)] for i in range(n)]
d = deque()
for i in range(n):
    for j in range(n):
        if i < j:
            if len(l[i][j]) > 0:
                for k in l[i][j]:
                    rl[k[0]][k[1]] += 1
#print(rl)
for i in range(n):
    for j in range(n):
        if i < j:
            if rl[i][j] == 0:
                d.append([[i,j],0])
al = []
key = 0
#print(l)
if len(d) == 0:
    key = 1
while len(d):
    #print(d)
    now,day = d.pop()
    day += 1
    if len(l[now[0]][now[1]]) == 0:
        al.append(day)
    else:
        for i in l[now[0]][now[1]]:
            if rl[i[0]][i[1]] == 1:
                rl[i[0]][i[1]] -= 1
                d.append([i,max(day,dl[i[0]][i[1]])])
            else:
                rl[i[0]][i[1]] -= 1
                dl[i[0]][i[1]] = max(day,dl[i[0]][i[1]])
    if day > n*(n-1)//2:
        key = 1
        break
md = 0
for i in range(n):
    md += sum(rl[i])
if key == 1 or md > 0:
    print(-1)
else:
    print(max(al))