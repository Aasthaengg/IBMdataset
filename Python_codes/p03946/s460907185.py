n, t = map(int, input().split())
aas = list(map(int, input().split()))
maxs = [0]*n
max_a = aas[-1]
for i in reversed(range(n)):
    maxs[i] = max_a
    if aas[i] > max_a:
        max_a = aas[i]
difs = [0]*n
for i in range(n):
    difs[i] = maxs[i] - aas[i]
print(difs.count(max(difs)))