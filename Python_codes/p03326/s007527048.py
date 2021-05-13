import numpy as np
n,m = map(int,input().split())
xyz = [list(map(int,input().split())) for i in range(n)]
xyz = np.array(xyz)
a = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
a = np.array(a)
ans = 0
temp = []
for i in a:
    temp = []
    b = i * xyz
    for j in b:
        temp.append(sum(j))
    temp.sort(reverse=1)
    ans = max(ans,sum(temp[:m]))
print(ans)