N,C = map(int,input().split())
sushi = [list(map(int,input().split())) for _ in range(N)]

R = [(0,0)]
L = [(0,0)]

for s in sushi:
    R.append((s[0],R[-1][1]+s[1]))

for s in sushi[::-1]:
    L.append((C-s[0],L[-1][1]+s[1]))

R_reversible = [False for _ in range(N+1)]
L_reversible = [False for _ in range(N+1)]

for i in range(N+1):
    if R[i][1]-2*R[i][0] >= 0:
        R_reversible[i] = True
    if L[i][1]-2*L[i][0] >= 0:
        L_reversible[i] = True
        
R_dif = [0 for _ in range(N+1)]
L_dif = [0 for _ in range(N+1)]

for i in range(N+1):
    R_dif[i] = R[i][1]-R[i][0]
    L_dif[i] = L[i][1]-L[i][0]
    
rmax = 0
lmax = 0

for i in range(N+1):
    if rmax > R_dif[i]:
        R_dif[i] = rmax
    if lmax > L_dif[i]:
        L_dif[i] = lmax
    rmax = max(rmax,R_dif[i])
    lmax = max(lmax,L_dif[i])
    
ans = max(rmax,lmax)

for i in range(1,N+1):
    if R_reversible[i]:
        ans = max(ans,R[i][1]-2*R[i][0]+L_dif[N-i])
    if L_reversible[i]:
        ans = max(ans,L[i][1]-2*L[i][0]+R_dif[N-i])

print(ans)