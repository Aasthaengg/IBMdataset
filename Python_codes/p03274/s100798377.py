def mips():
    return map(int,input().split())
N,K = mips()
C = [c for c in mips()]
dist = []
for i in range(N-K+1):
    dist.append(min(abs(C[i]) + abs(C[i+K-1]-C[i]),abs(C[i+K-1]) + abs(C[i+K-1]-C[i])))
print(min(dist))
