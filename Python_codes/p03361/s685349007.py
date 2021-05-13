h,w = map(int, input().split())
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            ok = False
            for x,y in [(1,0), (0,1), (-1, 0), (0,-1)]:
                new_h, new_w = i+x, j+y
                if new_h >= h or new_h < 0 or new_w >= w or new_w < 0: continue
                if s[new_h][new_w] == "#": 
                    ok = True
                    break
            if not ok:
                print("No")
                exit()
print("Yes")