N, K = map(int, input().split())
A = list(map(int, input().split()))

D = {}
for a in A:
    if a not in D:
        D[a] = 1
    else:
        D[a] += 1
E = sorted(D.values())
c = 0
i = 0
l = len(D)
while l > K:
    c += E[i]
    l -= 1
    i += 1
print(c)