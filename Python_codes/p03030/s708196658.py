
q = int(input())

r = set([])

g = {}

n = {}

for i in range(q):
    s,p = input().split()
    if s not in r:
        r.add(s)
        g[s] = [int(p)]
        n[int(p)] = i+1
    else:
        g[s].append(int(p))
        n[int(p)] = i+1
        
r = list(r)

r.sort()

for i in r:
    x = g[i]
    x.sort(reverse = True)
    for t in x:
        print(n[t])