import numpy as np
N,M = map(int,input().split())
L = np.array([list(map(int,input().split())) for _ in range(N)])
l = [[1,1,1],[1,1,-1],[1,-1,1],[-1,1,1],[1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,-1,-1]]
ans = 0
for i in range(8):
    su = L[:,0]*l[i][0]+L[:,1]*l[i][1]+L[:,2]*l[i][2]
    s = np.sort(su)[::-1]
    ans = max(ans,np.sum(s[:M]))
print(ans)