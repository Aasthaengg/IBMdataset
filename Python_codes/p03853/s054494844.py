import sys
input = sys.stdin.readline

H, W = map(int, input().split())
fig_ori = []
fig = []
for i in range(H):
    fig_ori.append(list(input().rstrip('\n')))
for i in range(2 * H):
    low = []
    for j in range(W):
        low.append(fig_ori[(i+1+1)//2-1][j])
    fig.append(low)

for i in range(2 * H):
    for j in range(W):
        print(fig[i][j], end='')
    print()
