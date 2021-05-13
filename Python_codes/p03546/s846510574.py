from collections import Counter
h,w = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(10)]
a = []
for i in range(h):
    a += list(map(int,input().split()))
C = Counter(a)
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])
ans = 0
for i,n in C.items():
    if i != -1:
        ans += c[i][1]*n
print(ans)