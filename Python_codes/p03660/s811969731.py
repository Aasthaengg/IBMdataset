N = int(input())
E = [[] for _ in [0]*N]
for _ in [0]*(N-1):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
V = [0]*N
V[0] = 1
V[-1] = -1
q = [0,N-1]
while q:
    qq = []
    for i in q:
        Vi = V[i]
        for j in E[i]:
            if not V[j]:
                V[j] = Vi
                qq.append(j)
    q = qq
print("Fennec" if sum(V)>0 else "Snuke")
