N=int(input())
AA=list(map(int,input().split()))
Lmax=0
for i in range(N):
    Lmax = max(Lmax,AA[i])
print("Yes" if Lmax<(sum(AA)-Lmax) else "No")