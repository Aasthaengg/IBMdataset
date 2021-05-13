s = input()
k = int(input())

cand = []

ilis = sorted(range(len(s)), key=lambda k: s[k])

visited = set()

for i in range(len(s)):
    for j in range(5):
        cand.append(s[ilis[i]:ilis[i]+j+1])

cand.sort()

ret = sorted(list(set(cand)))

print(ret[k-1])
