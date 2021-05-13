N,M=map(int,input().split())
Lmax = 0
Rmin = 1e8
for _ in range(M):
    L,R=map(int,input().split())
    if L > Lmax:
        Lmax = L
    if R < Rmin:
        Rmin = R

print(max(0, Rmin - Lmax + 1))