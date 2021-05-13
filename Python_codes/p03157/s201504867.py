from collections import deque
H,W = map(int, input().split())
S = [input() for _ in range(H)]

used = [[0]*W for _ in range(H)]
q = deque()
ans = 0
for i in range(H):
    for j in range(W):
        if used[i][j] == 1:
            continue
        if S[i][j] == ".":
            continue
        dic = {"#":1, ".":0}
        q.append((i, j, "#"))
        used[i][j] = 1
        while q:
            temp = q.popleft()
            k = temp[0]
            l = temp[1]
            f = temp[2]
            if f == "#":
                f = "."
            else:
                f = "#"
            if k > 0 and S[k-1][l] == f and used[k-1][l] == 0:
                used[k-1][l] = 1
                dic[f] += 1
                q.append((k-1, l, f))
            if k < H-1 and S[k+1][l] == f and used[k+1][l] == 0:
                used[k+1][l] = 1
                dic[f] += 1
                q.append((k+1, l, f))
            if l > 0 and S[k][l-1] == f and used[k][l-1] == 0:
                used[k][l-1] = 1
                dic[f] += 1
                q.append((k, l-1, f))
            if l < W-1 and S[k][l+1] == f and used[k][l+1] == 0:
                used[k][l+1] = 1
                dic[f] += 1
                q.append((k, l+1, f))
        ans += dic["#"]*dic["."]

print(ans)