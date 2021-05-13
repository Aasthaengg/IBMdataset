N,M = map(int,input().split())

L_max = 0
R_min = N

for i in range(M):
    L, R = map(int, input().split())
    R_min = min(R,R_min)
    L_max = max(L,L_max)

print(max(R_min-L_max+1,0))