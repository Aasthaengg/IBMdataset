h, w = map(int, input().split())
maze = []
def where(step):
    hh = step // w
    tmp = step - (w*hh)
    if hh % 2 == 0:
        ww = tmp
    else:
        ww = w-1-tmp
    return [hh, ww]

for _ in range(h):
    l = map(int, input().split())
    l = list(l)
    maze.append(l)

res = []
for i in range(h*w - 1):
    hh1, ww1 = where(i)
    hh2, ww2 = where(i+1)
    #print(hh1, ww1,hh2,ww2)
    if maze[hh1][ww1] % 2 == 1:
        maze[hh2][ww2] += 1
        res.append((hh1,ww1,hh2,ww2))
#print(res)

print(len(res))
for i in range(len(res)):
    a,b,c,d = res[i]
    print(a+1,b+1,c+1,d+1)
