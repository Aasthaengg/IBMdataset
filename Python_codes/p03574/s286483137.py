H,W = map(int, input().split())

S = ['.'*(W + 2)] + ['.' + input() + '.' for _ in range(H)] + ['.'*(W + 2)]

for x in range(1, H+1):
    for y in range(1, W+1):
        if S[x][y] == '.':
            Bomb = (S[x-1][y-1:y+2] + S[x][y-1:y+2] + S[x+1][y-1:y+2]).count('#')
            S[x] = S[x][:y] + str(Bomb) +S[x][y+1:]

for i in range(1, H+1):
    print(S[i][1:W+1])