H,W,S= map(int, input().split())
grid=[[v for v in input()] for _ in range(H)]

ans=H*W
for row in range(1<<(H-1)):
    row_cut = str(bin(row))[2:].count("1")
    splits = [grid[0]]
    for i in range(H-1):
        if row & (1<<i):
            splits.append(grid[i+1][:])
        else:
            splits[-1]=[splits[-1][j]+grid[i+1][j] for j in range(W)]

    if any(max(v.count("1") for v in s)>S for s in splits):
        continue

    count=[[] for _ in range(len(splits))]
    for i,s in enumerate(splits):
        for v in s:
            count[i].append(v.count("1"))

    col_cut=0
    tmp_cnt=[count[i][0] for i in range(len(splits))]
    for i in range(1,W):
        merged_cnt=[tmp_cnt[j]+count[j][i] for j in range(len(splits))]
        if max(merged_cnt)>S:
            col_cut+=1
            tmp_cnt =[count[j][i] for j in range(len(splits))]
        else:
            tmp_cnt=merged_cnt
    ans = min(ans,col_cut+row_cut)


print(ans)
    

