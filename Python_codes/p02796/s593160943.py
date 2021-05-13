from operator import itemgetter
N, *A = map(int, open(0).read().split())
X = [(x-l, x+l) for x, l in zip(*[iter(A)]*2)]
X.sort(key=itemgetter(1))
ans = 0
R = -float('inf')
for l, r in X:
    if R <= l:
        ans += 1
        R = r
print(ans)
