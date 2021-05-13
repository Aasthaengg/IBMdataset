n,m,c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
vecprod = [0] * n
for i,ln in enumerate(a):
    s = 0
    for j in range(m):
        s += ln[j] * b[j]
    vecprod[i] = s
vecprod = [1 if x + c > 0 else 0 for x in vecprod]
print(sum(vecprod))