N = int(input())
S = [input() for _ in range(N)]
c = {}

for s in S:
    if c.get(s):
        c[s] += 1
    else:
        c[s] = 1


s_items = sorted(c.items(), key=lambda x: x[1], reverse=True)
n_max = s_items[0][1]

print('\n'.join(sorted(map(lambda x: x[0], filter(lambda x: x[1] == n_max, s_items)))))