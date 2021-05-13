from collections import Counter
H,W=list(map(int, input().split()))
C=[list(map(int, input().split())) for _ in range(10)]
A=Counter()
for _ in range(H):
    A+=Counter(list(map(int, input().split())))
del A[-1]
# print(A)
# Warshall–Floydを使います

for i in range(10):
    via=C[i]
    for j in range(10):
        c=C[j]
        for k in range(10):
            c[k]=min(c[i]+via[k], c[k])
# print(C)

ans=0
for i in A:
    ans+=C[i][1]*A[i]
print(ans)