H,W,K=map(int,input().split(' '))
S=[input() for i in range(H)]
ans = [[0]*W for i in range(H)]
cnt = 1
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans[i][j] = cnt
            cnt += 1
def group(h,w,k):
    ans[h][w] = k
    if 0<=w+1<W and ans[h][w+1] == 0:
            group(h,w+1,k)
    if 0<=w-1<W and ans[h][w-1] == 0:
            group(h,w-1,k)
def group_h(h,w,k):
    ans[h][w] = k
    if 0<=h+1<H and ans[h+1][w] ==0:
        group_h(h+1,w,k)
    if 0<=h-1<H and ans[h-1][w] == 0:
        group_h(h-1,w,k)

for h,i in enumerate(ans):
    for w,j in enumerate(i):
        if j != 0:
            group(h,w,j)
for h,i in enumerate(ans):
    for w,j in enumerate(i):
        if j != 0:
            group_h(h,w,j)
for i in ans:
    for j in i:
        print(j,"",end="")
    print("")