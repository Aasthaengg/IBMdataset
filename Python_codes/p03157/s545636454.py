from collections import defaultdict

H, W = map(int, input().split())

S = [input() for _ in range(H)]




es = defaultdict(list)
for i in range(H):
    for j in range(W):

        # 縦の経路
        if i == 0 and H != 1:
            if S[i][j] != S[i+1][j]:
                es[(i,j)].append((i+1,j))
                es[(i+1,j)].append((i,j))
        elif 0 < i < H-1:
                if S[i][j] != S[i+1][j]:
                    es[(i,j)].append((i+1,j))
                    es[(i+1,j)].append((i,j))
                if S[i][j] != S[i-1][j]:
                    es[(i,j)].append((i-1,j))
                    es[(i-1,j)].append((i,j))
        elif i == H-1 and H != 1:
                if S[i][j] != S[i-1][j]:
                    es[(i,j)].append((i-1,j))
                    es[(i-1,j)].append((i,j))

        # 横の経路
        if j == 0 and W != 1:
            if S[i][j] != S[i][j+1]:
                es[(i,j)].append((i,j+1))
                es[(i,j+1)].append((i,j))
        elif 0 < j < W-1:
            if S[i][j] != S[i][j+1]:
                es[(i,j)].append((i,j+1))
                es[(i,j+1)].append((i,j))
                if S[i][j] != S[i][j-1]:
                    es[(i,j)].append((i,j-1))
                    es[(i,j-1)].append((i,j))
        elif j == W-1 and W != 1:
                if S[i][j] != S[i][j-1]:
                    es[(i,j)].append((i,j-1))
                    es[(i,j-1)].append((i,j))

checked = [[False for _ in range(W)] for H in range(H)]


ans = 0
for i in range(H):
    for j in range(W):
        if checked[i][j] == True:
            continue
        
        cnt_b = 0
        cnt_w = 0

        if S[i][j] == "#":
            cnt_b += 1
        else:
            cnt_w += 1
        checked[i][j] = True
        stack = es[(i,j)]

        while stack:
            new_stack = []
            for p,q in stack:
                if checked[p][q] == False:
                    checked[p][q] = True
                    if S[p][q] == "#":
                        cnt_b += 1
                    else:
                        cnt_w += 1

                    new_stack.extend(es[(p,q)])
            if len(new_stack) == 0:
                break
            else:
                stack = new_stack
        
        ans += cnt_b * cnt_w

print(ans)