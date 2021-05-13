h,w,d = map(int,input().split())
li = [-1]*h*w

for i in range(h):
    a = list(map(int,input().split()))
    for j in range(w):
        li[a[j]-1] = (i,j)

li2 = [[] for _ in range(d)]
li3 = [[0] for _ in range(d)]
for i in range(d):
    li_tmp = li[i::d]
    for j in range(len(li_tmp)-1):
        li2[i].append(abs(li_tmp[j][0]-li_tmp[j+1][0]) + abs(li_tmp[j][1]-li_tmp[j+1][1]))

for i in range(d):
    for j in range(len(li2[i])):
        if j == 0:
            li3[i].append(li2[i][j])
        else:
            li3[i].append(li3[i][-1] + li2[i][j])

q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    l1 = l % d
    print(li3[l1][r//d] - li3[l1][l//d])
