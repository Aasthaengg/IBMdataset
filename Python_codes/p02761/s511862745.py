n, m = map(int, input().split())
res = ["n" for _ in range(n)]
con = False
for _ in range(m):
    s, c = map(int, input().split())
    idx = s - 1
    if res[idx] == "n" or res[idx] == c:
        res[idx] = c
    if res[idx] != "n" and res[idx] != c:
        con = True
        break
if con or (n > 1 and res[0] == 0): print(-1)
else:
    if res[0] == "n":
        if n == 1:
            res[0] = 0
        else:
            res[0] = 1
    for i in range(1, n):
        if res[i] == "n": res[i] = 0
    print(int("".join([str(r) for r in res])))