N = int(input())
cnt = dict()

nodes = [set() for _ in range(N+1)]

for _ in range(N-1):
    a, b = [int(x) for x in input().split()]
    cnt[a-1] = cnt.get(a-1,0) + 1
    cnt[b-1] = cnt.get(b-1,0) + 1
    nodes[a-1].add(b-1)
    nodes[b-1].add(a-1)


C = [int(x) for x in input().split()]
C = sorted(C, reverse=True)

Z = cnt.items()
Z = sorted(Z, key=lambda x:x[1], reverse=True)
# print(Z)

opennodes = {Z[0][0]}
closednodes = set()

ans = [-1] * N


for i in range(N):
    n = opennodes.pop()
    closednodes.add(n)
    ans[n] = C[i]

    for nn in nodes[n]:
        if not nn in closednodes:
            opennodes.add(nn)

print(sum(C) - max(C))
print(" ".join([str(x) for x in ans]))


