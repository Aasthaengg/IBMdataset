def inpl(): return list(map(int, input().split()))
H,W = inpl()
MAP = [inpl() for i in range(H)]
flag = False #コインを持っているか
ans = []
for y in range(H):
    if y%2 == 0:
        xx = range(W)
    else:
        xx = reversed(range(W))
    for x in xx:
        if flag:
            ans.append([by,bx,y,x])
        if MAP[y][x]%2 == 1:
            flag = not flag
        bx,by = x,y
print(len(ans))
for a,zu,nya,n in ans:
    print(a+1,zu+1,nya+1,n+1)