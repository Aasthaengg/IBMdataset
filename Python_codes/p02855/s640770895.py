h,w,k = map(int,input().split())
s = [input() for i in range(h)]
ans = [[0]*w for i in range(h)]
c = 1
not_cherry = [] #イチゴがない列
ok = False
for i in range(h):
    if '#' in s[i]:
        cherry = 0
        for j in range(w):
            if s[i][j]=='#':
                if cherry==0:
                    ans[i][j] = c
                else:
                    c += 1
                    ans [i][j] = c
                cherry += 1
            else:
                ans[i][j] = c
        c += 1
        ok = False
    else:
        if ok:
            not_cherry[-1] += 1
        else:
            not_cherry.append(1)
        ok = True

i = 0
ind = 0
while i<h:
    if 0 in ans[i]:
        c = not_cherry[ind]
        for l in range(c):
            for j in range(w):
                if i+l<h-1 and i+c<h-1:ans[i+l][j] = ans[i+c][j]
                else:ans[i+l][j] = ans[i+l-1][j]
        i+=c
        ind += 1
    else:
        i+=1

for i in ans:
    print(*i)
      
