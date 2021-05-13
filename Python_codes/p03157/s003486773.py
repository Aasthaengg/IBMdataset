from collections import defaultdict

H, W = map(int, input().split())
field = [[c == '#' for c in input()] for _ in range(H)]
counted = [[False] * W for _ in range(H)]
detected = [[False] * W for _ in range(H)]

b_count = defaultdict(int)
w_count = defaultdict(int)
another_group = [(0, 0)]
group = 0
while another_group:
    i, j = another_group.pop()
    detected[i][j] = True
    if counted[i][j]:
        continue
    
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        if field[i][j]:
            b_count[group] += 1
        else:
            w_count[group] += 1
        #print(i, j, group)
        counted[i][j] = True
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= i+di < H and 0 <= j+dj < W:
                if not detected[i+di][j+dj]:
                    if field[i+di][j+dj] == field[i][j]:
                        another_group.append((i+di, j+dj))
                    else:
                        detected[i+di][j+dj] = True
                        stack.append((i+di, j+dj))
                
    group += 1         

ans = 0
for bk, bv in b_count.items():
    ans += bv * w_count[bk]

print(ans)