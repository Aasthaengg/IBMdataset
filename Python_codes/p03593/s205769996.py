h,w = map(int,input().split())
L = []
for i in range(h):
    L.append(input())
boo = []
for i in range(h):
    F = [False]*w
    boo.append(F)
numlist = []
cnt = 0
tate = 1
yoko = 1
if h == 1:
    if w == 1:
        numlist = [1]
    else:
        if w%2 != 0:
            for i in range(w//2):
                numlist.append(2)
            numlist.append(1)
        else:
            for i in range(w//2):
                numlist.append(2)
elif w == 1:
    if h%2 != 0:
        for i in range(h//2):
            numlist.append(2)
        numlist.append(1)
    else:
        for i in range(h//2):
            numlist.append(2)
else:
    while cnt != h*w:
        if boo[tate-1][yoko-1] == False:
            if h%2 == 1 and tate-1 == h//2:
                if w%2 == 1 and yoko-1 == w//2:
                    boo[tate-1][yoko-1] = True
                    numlist.append(1)
                    cnt += 1
                    yoko += 1
                else:
                    boo[tate-1][yoko-1] = True
                    boo[tate-1][w-yoko] = True
                    numlist.append(2)
                    cnt += 2
                    yoko += 1
            else:
                if w%2 == 1 and yoko-1 == w//2:
                    boo[tate-1][yoko-1] = True
                    boo[h-tate][yoko-1] = True
                    numlist.append(2)
                    cnt += 2
                    yoko += 1
                else:
                    boo[tate-1][yoko-1] = True
                    boo[h-tate][yoko-1] = True
                    boo[tate-1][w-yoko] = True
                    boo[h-tate][w-yoko] = True
                    numlist.append(4)
                    cnt += 4
                    yoko += 1
        else:
            yoko += 1
        if yoko == w:
            if tate != h:
                yoko = 1
                tate += 1
            else:
                break
list_alp = [0]*26
for i in range(h):
    for j in range(w):
        list_alp[ord(L[i][j])-97] += 1
temp = 0
flag = True
list_alp.sort()
list_alp.reverse()
numlist.sort()
numlist.reverse()
for i in range(len(numlist)):
    if list_alp[0] < numlist[temp]:
        flag = False
        break
    else:
        list_alp[0] -= numlist[temp]
        temp += 1
        list_alp.sort()
        list_alp.reverse()
if flag:
    if sum(list_alp) == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
