N, M = map(int, input().split())
d = {i + 1: [] for i in range(N)}

for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

ans = False
one_to_i = d[1]
for i in one_to_i:
    if N in d[i]:
        ans = True
        break

if ans:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

