from collections import deque

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

visited = [[False]*W for _ in range(H)]
ans = 0

for row in range(H):
    for col in range(W):
        if not visited[row][col]:
            visited[row][col] = True
            d = deque([[row, col]])
            if s[row][col] == ".":
                passed_black, passed_white = 0, 1
            else:
                passed_black, passed_white = 1, 0

            while d:
                now_row, now_col = d.popleft()
                visited[now_row][now_col] = True
                for new_row, new_col in [[now_row+1, now_col], [now_row-1, now_col], [now_row, now_col+1], [now_row, now_col-1]]:
                    if 0 <= new_row <= H-1 and 0 <= new_col <= W-1 and s[now_row][now_col] != s[new_row][new_col] and not visited[new_row][new_col]:
                        d.append([new_row, new_col])
                        visited[new_row][new_col] = True
                        if s[new_row][new_col] == ".":
                            passed_white += 1
                        else:
                            passed_black += 1

            ans += passed_black * passed_white

print(ans)