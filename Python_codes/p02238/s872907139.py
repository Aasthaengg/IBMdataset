from collections import deque
n = int(input())
u = []
k = []
v = []

for i in range(n):
    tmp = list(map(int, input().split()))
    u.append(tmp[0])
    k.append(tmp[1])
    if tmp[1] != 0:
        v.append(tmp[2:])
    else:
        v.append([])
        
check = [0]*n
intime = [0]*n
outtime = [0]*n
time = 1

def dfs(v, start):
    d = deque()
    d.append(start)
    global check
    global intime
    global outtime
    global time
    check[start-1] = 1
    intime[start-1] = time
    time += 1
    while len(d) > 0:
        visit = d[-1]
        tf = True
        for dtn in v[visit-1]:
            if check[dtn-1] == 0:
                d.append(dtn)
                check[dtn-1] = 1
                intime[dtn-1] = time
                time += 1
                tf = False
                break
        if tf:
            outtime[visit-1] = time
            d.pop()
            time += 1

dfs(v, 1)
for i in range(n):
    if check[i] == 0:
        dfs(v, i+1)
for i in range(n):
    print(i+1, intime[i], outtime[i])
