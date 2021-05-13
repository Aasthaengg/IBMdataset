N = int(input())
AB = [list(map(int,input().split())) for _ in [0]*(N-1)]

E = [{} for _ in [0]*N]
for a,b in AB:
    E[a-1][b-1] = 1
    E[b-1][a-1] = 1

def dist_dfs_tree(N,E,start):
    d = [-1]*N
    d[start] = 0
    q = [start]
    while q:
        i = q.pop()
        ci = d[i]
        for j,cj in E[i].items():
            if d[j] !=-1:continue
            d[j] = ci+cj
            q.append(j)
    return d

D1 = dist_dfs_tree(N,E,0)
Dn = dist_dfs_tree(N,E,N-1)
d1n = D1[-1]
for i,dd in enumerate(zip(D1,Dn)):
    if dd[0] == d1n//2 and sum(dd) == d1n:break

di = Dn[i]
for j in E[i]:
    if Dn[j]==di-1:break
E[i].pop(j)
E[j].pop(i)
s1 = sum(s>=0 for s in dist_dfs_tree(N,E,0))
print("Fennec" if s1 > N//2 else "Snuke")