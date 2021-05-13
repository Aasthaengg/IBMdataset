n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
V = []
C = []
for i in range(n):
    if v[i]>c[i]:
        V.append(v[i])
        C.append(c[i])
print(sum(V)-sum(C))