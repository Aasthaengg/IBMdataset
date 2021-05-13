n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]
t = [[] for _ in range(n + 1)]
for i in ab:
    t[i[1]].append(i[0])
flag = False
for j in t[n]:
    if 1 in t[j]:
        flag = True
        break
print("POSSIBLE") if flag else print("IMPOSSIBLE")