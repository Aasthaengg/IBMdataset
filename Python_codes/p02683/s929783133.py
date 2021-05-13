import numpy as np
n,m,x = list(map(int, input().split()))
masu = [list(map(int, input().split())) for _ in range(n)]
price = [masu[i][0] for i in range(n)]
skills = [masu[i][1:] for i in range(n)]



ans = 100000000000000
for idx_n in range(2**n):
    skill_sets = np.array([0 for _ in range(m)])
    total = 0
    #print(skill_sets.shape)
    for i_row, row in enumerate(skills):
        if idx_n & (2**i_row) >0:
            total += price[i_row]
            #print(np.array(row).shape)
            skill_sets += np.array(row)
    #print(skill_sets)
    if skill_sets.min() >= x:
        if ans >= total:
            ans = total
if ans == 100000000000000:
    print(-1)
else:
    print(ans)