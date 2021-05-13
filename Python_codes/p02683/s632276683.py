from itertools import combinations
n,m,x = map(int,input().split())
t = [list(map(int,input().split())) for i in range(n)]

ans = -1
for i in range(n+1):
    for comb in combinations(range(n),i):
        a = [0 for _ in [0]*m]
        c = 0
        for j in comb:
            temp = t[j]
            c += temp[0]
            for k in range(m):
                a[k] += temp[k+1]
        flag = True
        for j in a:
            if j<x:
                flag = False
                break
        if flag:
            if ans==-1:
                ans = c 
            else:
                ans = min(ans,c)

print(ans)