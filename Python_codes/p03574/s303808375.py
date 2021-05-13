h,w = map(int,input().split())
s = []
for i in range(h):
    s.append(list(input()))

dx = [-1,0,1,-1,1,-1,0,1]
dy = [1,1,1,0,0,-1,-1,-1]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        cnt = 0
        for t in range(8):
            ni=i+dx[t]
            nj=j+dy[t]
            if ni<0 or h<=ni: continue
            if nj<0 or w<=nj: continue
            if s[ni][nj] == '#':
                cnt += 1
        
        s[i][j] = str(cnt)

for i in s:
    print(''.join(i))