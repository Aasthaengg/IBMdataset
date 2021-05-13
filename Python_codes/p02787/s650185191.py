# E - Crested Ibis vs Monster
INF = 100000000
H,N = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
c = [INF]*H+[0]
for i in range(N):
    A,B = ab[i]
    for h in range(H,0,-1):
        k = max(0,h-A)
        c[k] = min(c[k], c[h]+B)
print(c[0])