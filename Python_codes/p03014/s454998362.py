H, W = map(int, input().split())

m = []
for i in range(H):
    m.append(input().rstrip('\n'))

wei = [[0]*(W+1) for _ in range(H+1)]
for h in range(H):
    for w in range(W):
        if m[h][w] == '.':
             wei[h][w] = wei[h][w-1] + 1
        else:
            wei[h][w] = 0
    #reverse
    for wz in range(W-1, -1, -1):
        if wei[h][wz] > 0 and wei[h][wz] < wei[h][wz+1]:
                wei[h][wz] = wei[h][wz + 1]

hei = [[0]*(W+1) for _ in range(H+1)]
for w in range(W):
    for h in range(H):
        if m[h][w] == '.':
             hei[h][w] = hei[h-1][w] + 1
        else:
            hei[h][w] = 0

    #reverse
    for hz in range(H-1, -1, -1):
        if hei[hz][w] > 0 and hei[hz][w] < hei[hz+1][w]:
            hei[hz][w] = hei[hz+1][w]

ans = 0
for h in range(H):
    for w in range(W):
       val = wei[h][w] + hei[h][w] - 1
       if ans < val:
           ans = val

print(ans)
