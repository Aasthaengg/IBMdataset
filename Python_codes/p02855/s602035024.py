h, w, k = map(int,input().split())
cak = [input() for i in range(h)]
nos = []
ans = [[-1 for i in range(w)] for j in range(h)]

for i,l in enumerate(cak):
    if not "#" in l:
        nos.append(i)

ni = 1
nh = -1
sf = True
for i,l in enumerate(cak):
    if sf and i in nos:
        continue
    elif i in nos:
        ans[i] = ans[i-1]
    else:
        lft = l.find("#")
        for j in range(lft+1):
            ans[i][j] = ni
        for j in range(lft+1,w):
            if l[j] == "#":
                ni += 1
            ans[i][j] = ni
        if sf:
            for j in range(i):
                ans[j] = ans[i]
            sf = False
        ni += 1

for l in ans:
    print(" ".join(map(str,l)))
