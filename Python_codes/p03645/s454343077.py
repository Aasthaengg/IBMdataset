r = [[] for _ in range(200001)] 
n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    r[a].append(b)

k = [1]
flag = 0
for _ in range(2):
    if flag == 1:
        break
    for j in k:
        kk = []
        kk += r[j]
        if n in r[j]:
            flag = 1
            break
    k = kk[:]

if flag == 1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")