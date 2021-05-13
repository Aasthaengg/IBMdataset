#import numpy as np
n,c=list(map(int,input().split()))
difference=[list(map(int,input().split())) for _ in range(c)]
base=[list(map(int,input().split())) for _ in range(n)]
#tmp_d=np.array(difference)
#tmp_b=np.array(base)
cal_col=[[0 for _ in range(c)] for _ in range(3)]
for i in range(n):
    for j in range(n):
        cal_col[(i+j)%3][base[i][j]-1]+=1
ans=float("inf")
for f_i in range(c):
    for s_i in range(c):
        for t_i in range(c):
            if f_i==s_i or f_i==t_i or s_i ==t_i:
                continue
            cal_val=0
            for n_i in range(c):
                cal_val+=difference[n_i][f_i]*cal_col[0][n_i]
                cal_val+=difference[n_i][s_i]*cal_col[1][n_i]
                cal_val+=difference[n_i][t_i]*cal_col[2][n_i]
            ans=min(ans,cal_val)

print(ans)