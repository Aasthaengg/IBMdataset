h , w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]
zyun = []
for i in range(1,h+1):
    if i % 2 == 1:
        for j in range(1,w+1):
            zyun.append((i,j))
    elif i % 2 == 0:
        for j in reversed(range(1,w+1)):
            zyun.append((i,j))
p = 0
cou = 0
ans = []
for y , x in zyun:
    if p == 0 and a[y-1][x-1] % 2 == 1:
        maey = y
        maex = x
        p = 1
    elif p == 1:
        ans.append([maey,maex,y,x])
        cou += 1
        if a[y-1][x-1] % 2 == 0:
            maey = y
            maex = x
        elif a[y-1][x-1] % 2 == 1:
            p = 0
print(cou)
for i in range(len(ans)):
    print(*ans[i])