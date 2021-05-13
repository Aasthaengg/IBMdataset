g = sorted([int(i) for i in input().split()])
if sum(g[:-1]) == g[-1]: print('Yes')
else: print('No')