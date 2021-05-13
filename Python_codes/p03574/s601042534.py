h, w = map(int, input().split())
S = [input() for _ in range(h)]

ans = [[-1]*w for _ in range(h)]

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [ 0, 0,-1, 1, -1, 1,  1,-1]

for i in range(h):
    for j in range(w):
        if S[i][j] == '#': continue
        ans[i][j] = 0
        for k in range(8):
            y = i + dy[k]
            x = j + dx[k]
            if y<0 or h<=y: continue
            if x<0 or w<=x: continue
            if S[y][x] == '#':
                ans[i][j] += 1

for i in range(h):
    for j in range(w):
        if ans[i][j] == -1:
            print('#',end='')
        else:
            print(ans[i][j],end='')
    print('')

# print(h,w)
# print(*S,sep='\n')
# print(*ans,sep='\n')
