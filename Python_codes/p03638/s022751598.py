from itertools import accumulate
H,W = map(int, input().split(' '))
n = int(input())
a = list(map(int, input().split(' ')))
ac = list(accumulate(a))
ansinv = [[0 for i in range(W)] for i in range(H)]
r = 1
k = 1
for i in range(H*W):
    if k > ac[r-1]:
        r += 1
    x = i//W
    y = i % W
    ansinv[x][y] = r
    k += 1
ans = ansinv
for i in range(H):
    if i % 2:
        ans[i] = ans[i][::-1]
for i in ans:
    print(*i, sep = " ")