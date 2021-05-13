N = int(input())

D = {}
q = set()
for i in range(N):
    s,p = input().split()
    if s in q:
        D[s].append([int(p),i])
    else:
        D[s] = [[int(p),i]]
        q.add(s)

ans = []
for i in sorted(list(q)):
    D[i].sort(reverse=True)
    for j in D[i]:
        ans.append(j[1])

[print(i+1) for i in ans]
