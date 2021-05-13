s = input()
x,y = map(int,input().split())
k = 0
data = [[],[]]
f = 0
p = 1
for s_ in s:
    if p==1 and s_=='F':
        x -= 1
        continue
    p = 0
    if s_ == 'T':
        if f:
            data[k].append(f)
        k = (k+1)%2
        f = 0
    else:
        f += 1
if f:
    data[k].append(f)

nx = sum(data[0])
ny = sum(data[1])

if nx<x or ny<y:
    print('No')
    exit()

dpx = [set() for _ in range(len(data[0])+1)]
dpy = [set() for _ in range(len(data[1])+1)]
dpx[0] |= {0}
dpy[0] |= {0}

for i in range(len(data[0])):
    k = data[0][i]
    for m in dpx[i]:
        dpx[i+1] |= {m+k,m-k}

for i in range(len(data[1])):
    k = data[1][i]
    for m in dpy[i]:
        dpy[i+1] |= {m+k,m-k}

if x in dpx[-1] and y in dpy[-1]:
    print('Yes')
else:
    print('No')