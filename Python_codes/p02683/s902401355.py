import numpy as np

N,M,X = map(int,input().split())
ca=np.array([0]*(M+1))
ans = 10**7

for i in range(N):
    ca=np.vstack([ca,[int(i) for i in input().split()]])

for i in range(2**N):

    need_skills=np.array([0]+[X]*M)

    buy_item = [0]*N
    for j in range(N):
        if (i>>j)&1:
            buy_item[j]=1

    for k in range(N):
        need_skills -= ca[k+1]*buy_item[k]

    if np.all(need_skills<=0):
        ans = min(ans,-need_skills[0])

print(-1 if ans==10**7 else ans)
