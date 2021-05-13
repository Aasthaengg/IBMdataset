h, w, d = map(int,input().split())
a = [list(map(int, input().split())) for i in range(h)]
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]

res = [[0] for i in range(d)]
memo = {} 
for i in range(h):
    for j in range(w):
        memo[a[i][j]] = (i, j)
res[0].append(0)
for i in range(1, w * h + 1):
    if i - d not in memo:
        res[i % d].append(0)
    else:
        wi, hi = memo[i]
        wii, hii = memo[i - d]
        diff = abs(wi - wii) + abs(hi - hii)
        res[i % d].append(diff)
        res[i % d][-1] += res[i % d][-2]

for l, r in query:
    mod = l % d
    l = l // d
    r = r // d
    print(res[mod][r + 1] - res[mod][l + 1])