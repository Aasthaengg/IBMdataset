import itertools
N = int(input())
r = int((N*2)**0.5)
if r * (r+1) == N*2:
    print('Yes')
    print(r+1)
    ans = [[r] for _ in range(r+2)]
    for i, c in enumerate(itertools.combinations(range(1, r+2), 2), start=1):
        ans[c[0]].append(i)
        ans[c[1]].append(i)
    for a in ans[1:]:
        print(*a)
else:
    print('No')
