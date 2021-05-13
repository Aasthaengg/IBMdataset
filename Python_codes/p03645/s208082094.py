n, m = map(int, input().split())
f = {}
s = {}


for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        f[b] = 1
        if b in s:
            print("POSSIBLE")
            exit()
    if b == n:
        s[a] = 1
        if a in f:
            print("POSSIBLE")
            exit()
print("IMPOSSIBLE")