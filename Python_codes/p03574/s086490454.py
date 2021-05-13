H, W = map(int, input().split())
S = ['.'+input()+'.' if i > 0 and i < H + 1 else '.' * (W+2) for i in range(H+2)]
for i in range(1, H+1):
    s = ''
    for j in range(1, W+1):
        if S[i][j] == '#': s += '#'
        else: s += str((S[i-1][j-1]+S[i-1][j]+S[i-1][j+1]+S[i][j-1]+S[i][j+1]+S[i+1][j-1]+S[i+1][j]+S[i+1][j+1]).count('#'))
    print(s)
