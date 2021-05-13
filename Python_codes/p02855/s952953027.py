h,w,k = map(int, input().split())
s = [None]*h
for i in range(h):
    s[i] = list(input())
ans = [[0 for i in range(w)] for j in range(h)]
ans2 = [[0 for i in range(w)] for j in range(h)]
cnt=1
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            ans[i][j] = cnt
            cnt+=1
piece=[0]*h
cnt=0
for i in range(h):
    for j in range(w):
        if ans[i][j] != 0:
            cnt+=1
            break
    piece[i] = cnt

for i in range(h):
    if piece[i] == 0:
        piece[i] = 1
for p in range(1,cnt+1):
    top=-1
    for j in range(h):
        if piece[j] == p:
            if top==-1:
                top=j
            bot=j

    beries=[]
    first_w=-1
    for j in range(w):
        berry=0
        for i in range(top,bot+1):
            if ans[i][j] != 0:
                berry=ans[i][j]
                if first_w==-1:
                    first_w = j
                    first_b = berry

        beries.append(berry)

    for j in range(first_w):
        beries[j] = first_b

    now_b = first_b
    for j in range(first_w,w):
        if beries[j] == 0:
            beries[j] = now_b
        else:
            now_b=beries[j]

    for i in range(top,bot+1):
        ans2[i] = beries


for row in ans2:
    print(*row,sep=" ")