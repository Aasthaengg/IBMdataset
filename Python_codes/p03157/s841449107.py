h,w=map(int,input().split())
s=[input() for _ in range(h)]

check = [[False for _ in range(w)]for __ in range(h)]

import queue
q=queue.Queue()
nh = [1,0,-1,0]
nw = [0,1,0,-1]

ans = 0
for i in range(h):
    for j in range(w):
        if check[i][j]:continue
        check[i][j] =True
        cnt = [0]*2
        cnt[s[i][j] == '#']+=1
        q.put([i,j])
        while not q.empty():
            nowi,nowj = q.get()
            for ne in range(4):
                ni = nowi + nh[ne]
                nj = nowj + nw[ne]
                if ni<0 or h <=ni or nj<0 or w<=nj:continue
                if s[nowi][nowj] == s[ni][nj]:continue
                if check[ni][nj]:continue
                check[ni][nj]=True
                cnt[s[ni][nj]=='#']+=1
                q.put([ni,nj])
        ans += cnt[0]*cnt[1]
print(ans)
