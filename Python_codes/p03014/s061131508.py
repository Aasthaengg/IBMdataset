H,W = map(int,input().split())
s = [input() for _ in range(H)]
ans = [[-1 for w in range(W)] for h in range(H)]
ans0 = ans[:]
for h in range(H):
    sh = s[h]
    st = -1
    gl = -1
    cnt = 0
    for w in range(W):
        if sh[w] == '.':
            cnt += 1
            if st == -1:
                st,gl = w,w
            gl +=1
            if w == W-1:
                for i in range(st,w+1):
                    ans[h][i] += cnt
        else:
            for i in range(st,gl):
                ans[h][i] += cnt
            cnt = 0
            st,gl = -1,-1
#print(*ans,sep='\n')
#ans1 = ans[:]
#ans = [[0 for w in range(W)] for h in range(H)]
for w in range(W):
    st = -1
    gl = -1
    cnt = 0
    for h in range(H):
        if s[h][w] == '.':
            cnt += 1
            if st == -1:
                st,gl = h,h
            gl +=1
            if h == H-1:
                for i in range(st,h+1):
                    ans[i][w] += cnt
        else:
            for i in range(st,gl):
                ans[i][w] += cnt
            cnt = 0
            st,gl = -1,-1
#print(*ans,sep='\n')
mx = 0
for x in ans:
    mx = max(max(x),mx)
print(mx)