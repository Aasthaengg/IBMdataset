import bisect
N,M,Q=map(int,input().split())
LR = []
for _ in range(M):
    LR.append(list(map(int,input().split())))
LR.sort()
L = [x for x,_ in LR]
R = [x for _,x in LR]

#事前に配列化 ans[i][j] i以降にスタート、j以前に完了の個数
ans = [[0]*510 for _ in range(510)]
for i in range(1,501):
    idx_L = bisect.bisect_left(L,i)
    arr=R[idx_L:]
    for ar in arr:
        ans[i][ar]+=1
    for j in range(1,501):
        ans[i][j]=ans[i][j-1]+ans[i][j]
    
for _ in range(Q):
    l,r = map(int,input().split())
    print(ans[l][r])
