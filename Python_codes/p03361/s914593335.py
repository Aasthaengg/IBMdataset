h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]
s.insert(0,[0]*w)
s.append([0]*w)

for i in range(h+2) :
    s[i].insert(0,0)
    s[i].append(0)

around = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(1,h+1) :
    for j in range(1,w+1) :
        if s[i][j] == '#' :
            ans = False
            for k in range(4) :
                if s[i-around[k][0]][j-around[k][1]] == '#' :
                    ans = True
            if not ans  :
                print('No')
                exit()
print('Yes')