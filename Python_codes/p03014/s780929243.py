h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))
lr = [[0] * w for i in range(h)]
#print(lr)
for i in range(h):
    cnt = 0
    lis = []
    for j in range(w):

        if s[i][j] == '#':
            lis.append(cnt)
            cnt = 0
        elif j == w-1:
            if s[i][j] == '.':
                cnt += 1
            lis.append(cnt)
        else:
            cnt += 1
    p = 0
    #print(lis)
    for j in range(w):
        if s[i][j] == '.':
            #print(p)
            #print(lr)
            lr[i][j] = lis[p]
        else:
            p += 1
#print(lr)

ud = [[0] * w for i in range(h)]
#print(ud)
for j in range(w):
    cnt = 0
    lis = []
    for i in range(h):
        #print(s[i][j])
        if s[i][j] == '#':
            lis.append(cnt)
            cnt = 0
        elif i == h-1:
            if s[i][j] == '.':
                cnt += 1
            lis.append(cnt)
        else:
            cnt += 1
    p = 0
    #print(lis)
    for i in range(h):
        #print(p,i,j,)
        #print(lis[p])
        #print(ud[j][i])
        if s[i][j] == '.':
            #print(p)
            #print(lr)
            ud[i][j] = lis[p]
        else:
            p += 1
        #print(p)
#print(ud)
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, lr[i][j] + ud[i][j] - 1)
print(ans)
