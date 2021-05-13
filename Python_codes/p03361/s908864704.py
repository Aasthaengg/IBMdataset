def main():
    H, W = map(int, input().split())
    s = [list(input()) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if s[y][x] == '.':
                continue
            else:
                for dx,dy in [-1,0],[0,-1],[1,0],[0,1]:
                    nx = x + dx
                    ny = y + dy
                    if (0 <= nx < W) and (0 <= ny < H) and s[ny][nx] != '.':
                        break
                    elif (0 > nx) or (W <= nx) or (0 > ny) or (H <= ny):
                        continue
                    elif dx == 0 and dy == 1 and s[ny][nx] == '.':
                        return 'No'

    return 'Yes'

print(main())
