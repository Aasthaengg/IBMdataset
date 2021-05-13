import numpy as np
N = int(input())
proof_list=np.array([[None]*N for i in range(N)])
check_list=[True]*N
for i in range(N):
    A = int(input())
    for j in range(A):
        x,y = map(int,input().split())
        proof_list[i][x-1] = y
ans = 0
for i in range(2**N):
    honests = []
    for j in range(N):
        if((i>>j)&1):
            honests.append(j)
    flag = True
    for l in honests:
        for k in range(N):
            if (k in honests) and proof_list[l][k] == 0:
                flag = False
            elif(k not in honests) and proof_list[l][k] ==1:
                flag = False
    if flag:
        ans = max(ans,len(honests))
print(ans)