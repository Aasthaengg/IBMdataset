s = input()
indices = {}

for i in range(len(s)):
    if s[i] in indices:
        indices[s[i]].append(i)
    else:
        indices[s[i]] = [-1, i]

minres = 1000

for key, value in indices.items():
    if len(value) > 1:
        dist = [value[i+1]-value[i] - 1 for i in range(len(value) - 1)]
    else:
        dist = [value[0]]

    res = max(max(dist), len(s)-value[-1]-1)
    if res < minres:
        minres = res

print(minres)