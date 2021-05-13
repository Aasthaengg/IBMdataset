H, W, K = map(int, input().split())
s = [list(input()) for _ in range(H)]

ans = [[-1]*W for _ in range(H)]

berry = []

for row in range(H):
    for col in range(W):
        if s[row][col] == "#":
            berry.append([row,col])

n = 0
for b in berry:
    n += 1
    row, col = b
    left, right = col, col
    ans[row][col] = n
    for c in range(col+1, W):
        if s[row][c] == "." and ans[row][c] == -1:
            right += 1
            ans[row][c] = n
        else:
            break
    for c in reversed(range(col)):
        if s[row][c] == "." and ans[row][c] == -1:
            left -= 1
            ans[row][c] = n
        else:
            break
    for r in range(row+1, H):
        for c in range(left, right+1):
            if s[r][c] == "#" or ans[r][c] != -1:
                break
        else:
            for c in range(left, right+1):
                ans[r][c] = n
            continue
        break
    for r in range(row):
        for c in range(left, right+1):
            if s[r][c] == "#" or ans[r][c] != -1:
                break
        else:
            for c in range(left, right+1):
                ans[r][c] = n
            continue
        break

for a in ans:
    print(*a)