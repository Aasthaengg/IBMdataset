# input
N = int(input())
X = list(map(int, input().split()))

# check
l, r = N // 2 - 1, N // 2
sort_x = sorted(X)
lx, rx = sort_x[l], sort_x[r]

if lx == rx:
    for i in range(N):
        print(lx)
else:
    for ind in range(N):
        target = X[ind]
        if target <= lx:
            print(rx)
        if target >= rx:
            print(lx)
