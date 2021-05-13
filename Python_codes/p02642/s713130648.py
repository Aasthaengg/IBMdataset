from collections import Counter
n = int(input())
A = list(map(int,input().split()))
mx = max(A)
C = Counter(A)
D = {a:True for a in A}
for a in A:
    if C[a]>1: D[a]=False
    for i in range(a*2, mx+1, a):
        D[i]=False
print(sum([D[a] for a in A]))