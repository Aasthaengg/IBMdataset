H, W = map(int, input().split())
S = [0]*(H+2)
S[0] = '*'*(W+2)
S[H+1] = '*'*(W+2)
for h in range(1,H+1):
    S[h] = '*' + input() + '*'

left = [[0]*(W+1) for _ in range(H+1)]
right = [[0]*(W+1) for _ in range(H+1)]
up = [[0]*(W+1) for _ in range(H+1)]
down = [[0]*(W+1) for _ in range(H+1)]

for h in range(1,H+1):
    for w in range(1,W+1):
        if S[h][w-1] in ['#','*'] or S[h][w]=='#':
            left[h][w] = 0
        else:
            left[h][w] = left[h][w-1]+1

for h in range(1,H+1):
    for w in range(W,0,-1):
        if S[h][w+1] in ['#','*'] or S[h][w]=='#':
            right[h][w] = 0
        else:
            right[h][w] = right[h][w+1]+1

for w in range(1,W+1):
    for h in range(1,H+1):
        if S[h-1][w] in ['#','*'] or S[h][w]=='#':
            up[h][w] = 0
        else:
            up[h][w] = up[h-1][w]+1

for w in range(1,W+1):
    for h in range(H,0,-1):
        if S[h+1][w] in ['#','*'] or S[h][w]=='#':
            down[h][w] = 0
        else:
            down[h][w] = down[h+1][w]+1
ans = 0
for h in range(1,H+1):
    for w in range(1,W+1):
        ans = max(ans,left[h][w]+right[h][w]+up[h][w]+down[h][w]+1)

print(ans)