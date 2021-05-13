from collections import deque
H, W = map(int, input().split())
s_list = []
for _ in range(H):
    s = input()
    s_list.append(s)
ans = 0
visited = set({})
for h in range(H):
    for w in range(W):
        if s_list[h][w] == '.':
            if str(h) + '_' + str(w) not in visited:
                d = deque()
                d.append([h, w])
                plus = 1
                minus = 0
                while d:
                    i, j = d.pop()
                    visited.add(str(i) + '_' + str(j))
                    for ii, jj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        if (0 <= (i + ii) < H) & (0 <= (j + jj) < W):
                            if str(i + ii) + '_' + str(j + jj) not in visited:
                                if s_list[i][j] != s_list[i + ii][j + jj]:
                                    d.append([i + ii, j + jj])
                                    visited.add(str(i + ii) + '_' + str(j + jj))
                                    if s_list[i + ii][j + jj] == '.':
                                        plus += 1
                                    else:
                                        minus += 1                                
                ans += plus * minus
print(ans)