H, W = map(int,input().split())

ans = [['0' for i in range(W)] for j in range(H)]

for i in range(H):
    S = input()
    for j,s in enumerate(S):
        if s == '#':
            ans[i][j] = '#'
            for a in range(-1,2):
                for b in range(-1,2):
                    if i+a >= 0 and j+b >= 0\
                        and i+a < H and j+b < W\
                        and ans[i+a][j+b] != '#':
                        ans[i+a][j+b] = str(int(ans[i+a][j+b])+1)

for i in range(H):
    print("".join(ans[i]))