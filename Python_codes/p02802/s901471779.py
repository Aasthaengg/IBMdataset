n, m = map(int, input().split())

ac = set()
wa = {}

for i in range(m):
    p, s = input().split()
    if s == 'AC':
        ac.add(p)
        wa[p] = wa.get(p, 0)
    else:
        if not p in ac:
            wa[p] = wa.get(p, 0)+1

ans = sum([wa[i] for i in ac])

print(len(ac), ans)

