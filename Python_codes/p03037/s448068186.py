N, M = map(int, input().split())
I = []
for _ in range(M):
    I.append(list(map(int, input().split())))

u = 0
o = 10 ** 9
for i in range(M):
    u = max(u, I[i][0])
    o = min(o, I[i][1])

if u > o:
    print(0)
else:
    print(o-u+1)