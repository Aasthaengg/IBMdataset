H,W = map(int, input().split())
fields = [list(input()) for i in range(H)]
# print(fields)

# seen = [False] * (H*W+1)
seen = [[False] * W for i in range(H)]
mv = [(0,1),(0,-1),(1,0),(-1,0)]
from collections import deque
from collections import defaultdict
ans  = 0
for i in range(H):
    for j in range(W):
        if seen[i][j]: continue
        # print("i,j",i,j)
        d = defaultdict(int)
        q = deque()
        q.append((i,j))
        # d[fields[i][j]] += 1
        while len(q) > 0:
            h,w = q.popleft()
            s = fields[h][w] #そこの文字列
            for dh, dw in mv:
                if 0 <= h + dh < H and 0 <= w + dw < W:
                    if seen[h+dh][w+dw]:continue
                    t = fields[h+dh][w+dw] #隣接セルの文字
                    if t == s:continue #同じ場合は加算せず
                    # print(s,t,h,w,h+dh,w+dw,"debug")
                    d[s] += 1
                    q.append((h+dh,w+dw))
                    seen[h+dh][w+dw] = True
        ans += d["#"]*d["."]
# print(seen)
print(ans)