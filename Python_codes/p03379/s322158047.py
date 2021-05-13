N = int(input())
X = list(map(int, input().split()))
order = {}
for idx, x in enumerate(X):
    order[idx] = x

X.sort()
m = N // 2
l = X[m - 1]
r = X[m]

for idx in range(N):
    x = order[idx]
    if x <= l:
        print(r)
    else:
        print(l)
